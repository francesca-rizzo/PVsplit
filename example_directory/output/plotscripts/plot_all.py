########################################################################
#### This script simply calls all other python scripts for plotting ####
########################################################################
import os 

scriptdir = '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_02_s64_h3043/serra_02_snap_64_h3043_i_1.05_2.3_1_3/output/serra_02_snap_64_h3043_i_1.05_2.3_1_3.alma_0.1arcsec_0/plotscripts/' 
cmd = '' 

for f in os.listdir(scriptdir): 
	if '.py' in f and f!='plot_all.py': 
		cmd += 'python %s/%s & '%(scriptdir,f) 

os.system(cmd[:-2]) 
