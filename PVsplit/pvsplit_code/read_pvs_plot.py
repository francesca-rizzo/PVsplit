import os
from pathlib import Path

def find_outfolder(output_folder):
    for item in os.listdir(output_folder):
        if os.path.isdir(os.path.join(output_folder, item)):
            if item.endswith('pvs'):
                outfolder = Path(output_folder)
    return outfolder

def fetch_pvs_plit(outfolder, paths):
    for item in os.listdir(outfolder):
        if os.path.isdir(os.path.join(outfolder, item)):
            fetch_pvs_plit(os.path.join(outfolder, item), paths)
        else:
            if item.endswith('plot_pvs.py'):
                paths.append(os.path.join(outfolder, item))

def open_plot_and_get_parameters(paths):
    zmin, zmax, zmin_wcs, zmax_wcs, ceiling = 0, 0, 0, 0, 0
    lines = None
    for filename in paths:
        if 'plot_pvs.py' in filename:
            f = open(filename, 'r')
            data = f.read()
            lines = data.split("\n")
    for i in lines:
        if "zmin, zmax" in i:
            sep_1 = i.split("=")
            numbers_1 = sep_1[1].strip().split(",")
            zmin = int(numbers_1[0])
            zmax = int(numbers_1[1].strip())
        elif "zmin_wcs, zmax_wcs" in i:
            sep_2 = i.split("=")
            numbers_2 = sep_2[1].strip().split(",")
            zmin_wcs = float(numbers_2[0])
            zmax_wcs = float(numbers_2[1].strip())
        elif "xminpv, xmaxpv" in i:
            sep_3 = i.split(",")
            numbers_3 = sep_3[2].strip()
            numbers_3 = numbers_3.strip(")").split("+")
            ceiling = int(numbers_3[1])

    return zmin, zmax, zmin_wcs, zmax_wcs, ceiling

#Check cdelt units in fits file
def check_units():
    # check the serra files
    pass