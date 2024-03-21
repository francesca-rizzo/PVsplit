import read_pvs_plot
import perform_pvsplit
import outputs

def main():
    input_folder = "/Users/francescarizzo/Documents/projects/refactored_pvsplit-main-2_final/example_directory/output" # Path to the folder containing the “pvs” and “plotscripts” directories
    gname = "serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0" # Name of the output files in the pvs folder
    outfolder = read_pvs_plot.find_outfolder(input_folder)
    paths = []
    p = read_pvs_plot.fetch_pvs_plit(outfolder, paths)
    zmin, zmax, zmin_wcs, zmax_wcs, ceiling = read_pvs_plot.open_plot_and_get_parameters(paths)
    p_major, p_minor1, p_minor2, p_v, p_r = perform_pvsplit.perform_pvsplit(outfolder, gname, zmin, zmax, zmin_wcs, zmax_wcs, ceiling)
    pvsplit_output_directory = outputs.create_output_directory(input_folder)
    outputs.write_to_text(p_major, p_minor1, p_minor2, p_v, p_r, pvsplit_output_directory)
    outputs.draw_3d_plots(p_major, p_v, p_r, pvsplit_output_directory)

main()