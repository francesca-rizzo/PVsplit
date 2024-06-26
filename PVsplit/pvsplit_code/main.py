import read_pvs_plot
import perform_pvsplit
import outputs

def main():
    input_folder = "../example_directory/output" # Path to the folder containing the “pvs” and “plotscripts” directories
    gname = "serra_02_snap_64_h3043_i_1.05_2.3_1.3.alma_0.1arcsec_0" # Name of the output files in the pvs folder
    outfolder = read_pvs_plot.find_outfolder(input_folder)
    paths = []
    p = read_pvs_plot.fetch_pvs_plit(outfolder, paths)
    zmin, zmax, zmin_wcs, zmax_wcs, ceiling = read_pvs_plot.open_plot_and_get_parameters(paths)
    p_major, p_minor1, p_minor2, p_v, p_r = perform_pvsplit.perform_pvsplit(outfolder, gname, zmin, zmax, zmin_wcs, zmax_wcs, ceiling)
    pvsplit_output_directory = outputs.create_output_directory(input_folder)
    outputs.write_to_text(p_major, p_minor1, p_minor2, p_v, p_r, pvsplit_output_directory)
    outputs.draw_3d_plots(p_major, p_v, p_r, pvsplit_output_directory)

main()
