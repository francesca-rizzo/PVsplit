import numpy as np

# Compute the parameters p_major, p_minor1 and p_minor2 mentioned in section 7.1 of the paper given input values of 
# position-velocity diagrams in both the major and minor axes.
def asymmetric_pv(pv_major_1, pv_major_2, pv_minor_1, pv_minor_2, pv_minor_3, pv_minor_4): 

	# Compute similarity and normalise between upper and lower regions of postion-velocity diagrams in the major axis
	a11 = (np.abs(pv_major_1 - pv_major_2) * np.abs(pv_major_1 - pv_major_2))
	a22 = (np.abs(pv_major_1 + pv_major_2) * np.abs(pv_major_1 + pv_major_2))

	# Computer p_major
	p_major = np.nansum(a11) / np.nansum(a22)
	
	# Compute similarity and normalise between upper and lower regions of postion-velocity diagrams in the minor axis
	b11 = (np.abs(pv_minor_1 - pv_minor_2) * np.abs(pv_minor_1 - pv_minor_2))
	b111 = (np.abs(pv_minor_1 + pv_minor_2) * np.abs(pv_minor_1 + pv_minor_2))
	b22 = (np.abs(pv_minor_3 - pv_minor_4) * np.abs(pv_minor_3 - pv_minor_4))
	b222 = (np.abs(pv_minor_3 + pv_minor_4) * np.abs(pv_minor_3 + pv_minor_4))
	
	# Compute p_minor_1 and p_minor_2 values
	p_minor_1 = np.nansum(b11) / np.nansum(b111)
	p_minor_2 = np.nansum(b22) / np.nansum(b222)
	
	return p_major, p_minor_1, p_minor_2