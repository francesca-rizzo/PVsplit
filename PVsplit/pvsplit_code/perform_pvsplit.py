import numpy as np
import os 
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path

import asymmetric_parameters
from select_20 import select_20_brightest as sel_20

def read_fits(outfolder, gname):

    outfolder = str(outfolder) + '/pvs/'
     # Position-velocity diagram in the major axis
    image_maj     = fits.open(outfolder + gname + '_pv_a.fits')
    # Position-velocity diagram in the minor axis 
    image_min     = fits.open(outfolder + gname + '_pv_b.fits')
    # Mask for position-velocity diagram in the major axis 
    image_mas_maj = fits.open(outfolder + gname + 'mask_pv_a.fits')
    # Mask for position-velocity diagram in the minor axis 
    image_mas_min = fits.open(outfolder + gname + 'mask_pv_b.fits')

    return image_maj, image_min, image_mas_maj, image_mas_min

def pixel_coordinates(head, ceiling):
     # Pixel coordinates of the central pixel of the position-velocity diagram
    crpixpv = np.array([head[0]['CRPIX1'],head[1]['CRPIX1']]) 
    cdeltpv = np.array([head[0]['CDELT1'],head[1]['CDELT1']]) 
    crvalpv = np.array([head[0]['CRVAL1'],head[1]['CRVAL1']]) 

    # Pixel coordinates of the edges of the position-velocity diagram
    xminpv, xmaxpv = np.floor(crpixpv - 1 - ceiling), np.ceil(crpixpv - 1 + ceiling)

     # Check if the pixel coordinates are within the range of the position-velocity diagram
    if xminpv[0]<0: 
        xminpv[0]=0 
    if xminpv[1]<0: 
        xminpv[1]=0 
    if xmaxpv[0]>=head[0]['NAXIS1']: 
        xmaxpv[0]=head[0]['NAXIS1']-1 
    if xmaxpv[1]>=head[1]['NAXIS1']: 
        xmaxpv[1]=head[1]['NAXIS1']-1

    #Return the pixel coordinates of the position-velocity diagram
    return crpixpv, cdeltpv, crvalpv, xminpv, xmaxpv

def read_data(image_maj, image_min, image_mas_maj, image_mas_min, zmin, zmax, xminpv, xmaxpv):
    # Data of the position-velocity diagram in the major and minor axes
    data_maj = image_maj[0].data[zmin:zmax+1,int(xminpv[0]):int(xmaxpv[0])+1] 
    data_min = image_min[0].data[zmin:zmax+1,int(xminpv[1]):int(xmaxpv[1])+1] 
    data_mas_maj = image_mas_maj[0].data[zmin:zmax+1,int(xminpv[0]):int(xmaxpv[0])+1] 
    data_mas_min = image_mas_min[0].data[zmin:zmax+1,int(xminpv[1]):int(xmaxpv[1])+1] 

    #Return the data of the position-velocity diagram in the major and minor axess
    return data_maj, data_min, data_mas_maj, data_mas_min

def write_to_fits(outfolder, pv20_1, pv20_2, pva_1, pva_2):

    outfolder = str(outfolder)
    # Save the results
    fits.writeto(outfolder + 'pva1.fits', pva_1, overwrite = True)
    fits.writeto(outfolder + 'pva2.fits', pva_2, overwrite = True)

    fits.writeto(outfolder + 'sel20_pva1.fits', pv20_1, overwrite = True)
    fits.writeto(outfolder + 'sel20_pva2.fits', pv20_2, overwrite = True)

def perform_pvsplit(outfolder, gname, zmin, zmax, zmin_wcs, zmax_wcs, ceiling):
    # Read the fits file
    rad, vrot, inc, pa, vsys = np.genfromtxt(str(outfolder) + '/rings_final2.txt', usecols = (1, 2, 4, 5, 11), unpack = True) 

    image_maj, image_min, image_mas_maj, image_mas_min = read_fits(outfolder, gname)

    # Header of the major and minor minor position-velocity diagram 
    head = [image_maj[0].header,image_min[0].header]

    # Pixel coordinates of the central pixel of the position-velocity diagram
    crpixpv, cdeltpv, crvalpv, xminpv, xmaxpv = pixel_coordinates(head, ceiling)

    # Data of the position-velocity diagram in the major and minor axes
    data_maj, data_min, data_mas_maj, data_mas_min = read_data(image_maj, image_min, image_mas_maj, image_mas_min, zmin, zmax, xminpv, xmaxpv)

    # Convert pixel coordinates to world coordinates
    xmin_wcs = ((xminpv+1-crpixpv)*cdeltpv+crvalpv)*3600 #modified by fra
    xmax_wcs = ((xmaxpv+1-crpixpv)*cdeltpv+crvalpv)*3600 

    #Compute line of sight velocity on the semi major axes
    radius = np.concatenate((rad,-rad)) 
    vlos1 = vrot * np.sin(np.deg2rad(inc))
    vlos2 = vrot * np.sin(np.deg2rad(inc)) 
    
    #Compute systemic velocity
    vsys_m = np.nanmean(vsys) 
    
    #Compute the extremities of the position-velocity diagram in the major and minor axes
    ext = [[xmin_wcs[0],xmax_wcs[0],zmin_wcs-vsys_m,zmax_wcs-vsys_m],\
		   [xmin_wcs[1],xmax_wcs[1],zmin_wcs-vsys_m,zmax_wcs-vsys_m]]
    
    #Compute the standard deviation of the position-velocity diagram in the major axis
    std_maj = data_maj*(np.abs(data_mas_maj-1))
    sigma = np.std(std_maj)
    
    #Create a mask for the position-velocity diagram in the major and minor axes
    mask_maj = np.zeros(shape = np.shape(data_maj))
    mask_min = np.zeros(shape = np.shape(data_min))

    #Remove noise from the position-velocity diagram in the major and minor axes
    mask_maj[data_maj > 3.*sigma] = 1
    mask_min[data_min > 3.*sigma] = 1
    
    #Compute new position-velocity diagram in the major and minor axes after removing noise
    data_maj=data_maj*mask_maj
    data_min=data_min*mask_min

    #Compute the pixel size and pixels along the line of sight
    cdelt = (ext[0][2] - ext[0][3]) / (zmax + 1 - zmin)
    zmean = int(np.round(ext[0][2] / cdelt))

    #Compute the number of pixels along the major and minor axes
    xmaj=int(np.round(xmaxpv[0] + 1 - xminpv[0]))
    xmin=int(np.round(xmaxpv[1] + 1 - xminpv[1]))
    
    #Split the position-velocity diagram into A1 and A2 regions
    pva_1=data_maj[0:zmean,:] #modified by fra
    pva_2=data_maj[zmean:,:]

    #Checking dimensions of A1 and A2 regions
    z1 = np.shape(pva_1)[0]
    z2 = np.shape(pva_2)[0]
    
    #Check if the dimensions of A1 and A2 regions are the same
    if(z1>z2):
        pva_2_copy = np.zeros(shape=(z1,np.shape(pva_1)[1]))
        pva_2_copy[0:z2,:]=pva_2
        pva_2 = pva_2_copy
    else:
        pva_1_copy = np.zeros(shape=(z2,np.shape(pva_1)[1]))
        pva_1_copy[z2-z1:,:]=pva_1
        pva_1 = pva_1_copy

    #Flip the position-velocity diagram along the major axis for the A2 region
    pva_2 = np.flip(pva_2)

    #Split the position-velocity diagram along the minor axis into B1, B2, B3 and B4 regions
    pvb_1 = data_min[:,0:xmin//2]
    pvb_2 = data_min[:,xmin//2+xmin%2:]
    pvb_3 = data_min[0:zmean,:]
    pvb_4 = data_min[zmean:,:]

    #Flipping B2 and B3 regions along the minor axis
    pvb_2=np.flip(pvb_2, axis=1)
    pvb_3=np.flip(pvb_3, axis=0)

    #Checking dimensions of B1, B2, B3 and B4 regions
    z3 = np.shape(pvb_3)[0]
    z4 = np.shape(pvb_4)[0]
    
    #Check if the dimensions of B3 and B4 regions are the same
    if(z4>z3):
        pvb_3_copy = np.zeros(shape=(z4,np.shape(pvb_4)[1]))
        pvb_3_copy[0:z3,:]=pvb_3
        pvb_3 = pvb_3_copy
    else:
        pvb_4_copy = np.zeros(shape=(z3,np.shape(pvb_4)[1]))
        pvb_4_copy[z3-z4:,:]=pvb_4
        pvb_4 = pvb_4_copy

    # Calculate P_major, P_minor1 and P_minor2 values mentioned in section 7.1 of the paper  
    a1, b1, b2 = asymmetric_parameters.asymmetric_pv(pva_1, pva_2, pvb_1, pvb_2, pvb_3, pvb_4)

    # Compute the parameters P_v and P_r corresponding to equations 6 and 7 mentioned in the paper
    pv20_1, deltaw1, deltaw11 = sel_20(pva_1, vlos1, vlos2, rad, (cdeltpv[0]*3600), head[0]['CDELT2']/1e+3)
    pv20_2, deltaw2, deltaw22 = sel_20(pva_2, vlos1, vlos2, rad, (cdeltpv[0]*3600), head[0]['CDELT2']/1e+3)

    # Compute the parameters P_v and P_r corresponding to d2 and d3 mentioned in the paper
    d2 = (deltaw1+deltaw2) / 2.0
    d3 = (deltaw11+deltaw22) / 2.0


    return np.log(a1), b1, b2, np.log(np.abs(d2-1)), d3 
