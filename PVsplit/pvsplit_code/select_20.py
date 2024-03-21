import numpy as np
from skimage.measure import label
from skimage.morphology import binary_dilation, remove_small_objects

# Used to Compute the parameters P_v and P_r corresponding to equations 6 and 7 mentioned in the paper
# given position-velocity diagrams in the major axis and velocity along the line of sight, radii, pixel size on the x and y axes.
def select_20_brightest(data, vlos1, vlos2, r, cdelt1, cdelt2):
	# Compute dimension of position-velocity diagram
	dim1 = np.shape(data)[1]
	dim2 = np.shape(data)[0]
	x = np.linspace(-dim1/2, dim1/2, dim1)
	y = np.linspace(dim2, 1, dim2)

	# Create a grid of linear spaced values based on dimensions of positon-velocity diagram
	xx, yy = np.meshgrid(x, y)
	
	# Compute the mean velocity along the line of sight
	vmean = (np.abs(vlos1) + np.abs(vlos2)) / 2.0
	vflat = np.mean(vmean[len(vmean)-2:])

	# Find top 20% brightest pixels in the position-velocity diagram
	data_1 = data[np.abs(data) != 0.00]
	data_1 = data_1.flatten()
	indx_1 = np.argsort(data_1)[::-1]
	cums_1 = (data_1[indx_1].cumsum() < 0.2 * np.sum(data_1)).argmin()

	# Finding the position of the above pixels in the position-velocity diagram
	pos = data_1[indx_1][:cums_1]

	# Redo
	mask = np.zeros(shape = np.shape(data))
	for j in np.arange(0, len(pos)):
		a = np.where(data == pos[j])
		mask[a] = 1
		
	new = data * mask
	
	# Removing outliers of bright pixels which are not part of groups
	new_small  = remove_small_objects(new != 0,min_size = 2)
	# Connecting small bright objects together
	new_dilate = binary_dilation(new_small != 0)

	# Compute the number of groups of bright pixels
	blobs, num_blobs = label(new_dilate,background = 0,return_num = True, connectivity = None)
	blobs[new_small == 0] = 0

	# Compute centroid of each group of bright pixels in the position-velocity diagram
	delta_v = np.zeros(shape = num_blobs)
	w = np.zeros(shape = num_blobs)
	w2 = np.zeros(shape = num_blobs)
	for k in np.arange(0, num_blobs):
		yclump = yy[blobs == k+1]
		xclump = xx[blobs == k+1]
		pos_clump = new[blobs == k+1]

		if (len(pos_clump)>3):
		
			xc = np.sum(pos_clump * xclump) / np.sum(pos_clump)
			yc = np.sum(pos_clump * yclump) / np.sum(pos_clump)	

			delta_v[k] = (yc * cdelt2) / vflat
			w[k] = np.abs(np.percentile(yclump, 2.3) - np.percentile(yclump, 97.7)) / yc
			w2[k] = np.abs(xc * cdelt1) / r[len(r)-1]


	return new, np.max(np.abs(delta_v)*np.exp(-w)), np.max(w2)