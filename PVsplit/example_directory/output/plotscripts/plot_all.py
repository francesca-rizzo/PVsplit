########################################################################
#### This script simply calls all other python scripts for plotting ####
########################################################################
import os 

scriptdir = '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/plotscripts/' 
cmd = '' 

for f in os.listdir(scriptdir): 
	if '.py' in f and f!='plot_all.py': 
		cmd += 'python %s/%s & '%(scriptdir,f) 

os.system(cmd[:-2]) 
