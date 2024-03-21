set terminal postscript eps enhanced color font 'Helvetica,14'
set output '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0_rc_inc_pa.eps'
unset key
set size 0.60, 1
set style line 1 lc rgb '#A9A9A9' lt 4 pt 7 lw 1
set style line 2 lc rgb '#B22222' lt 9 pt 9 lw 1
set macros
XTICS   = 'set xtics 0.050000; set mxtics 2; set format x "%g" '
NOXTICS = 'unset xlabel; set xtics  0.050000; set mxtics 2; set format x '' '
LABELF  = 'set xlabel font "Helvetica,13"; set ylabel font "Helvetica,13" '
TICSF   = 'set xtics font "Helvetica,12"; set ytics font "Helvetica,12" '
TMARGIN = 'set tmargin at screen 0.95; set bmargin at screen 0.47; set lmargin at screen 0.10; set rmargin at screen 0.50'
MMARGIN = 'set tmargin at screen 0.47; set bmargin at screen 0.27; set lmargin at screen 0.10; set rmargin at screen 0.50'
BMARGIN = 'set tmargin at screen 0.27; set bmargin at screen 0.10; set lmargin at screen 0.10; set rmargin at screen 0.50'
set multiplot layout 3,1 rowsfirst
@LABELF
@TICSF
@TMARGIN
@NOXTICS
set yrange [-5:302.09]
set ylabel 'V_c  [km/s]'
set ytics 50
set mytics 5
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:3:($3+$13):($3+$14) w errorbars ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:3 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:3:($3+$13):($3+$14) w errorbars ls 2, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:3 w lp ls 2
set title ''
@MMARGIN
@NOXTICS
set yrange [68.2527:83.42]
set ylabel 'i [deg]'
set ytics 5
set mytics 5
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:5:($5+$17):($5+$18) w errorbars ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:5 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:5 w lp ls 2
@BMARGIN
@XTICS
set xlabel 'Radius [arcsec]'
set yrange [245.864:320.988]
set ylabel 'P.A. [deg]'
set ytics 5
set mytics 5
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:6:($6+$19):($6+$20) w errorbars ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:6 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:6 w lp ls 2
unset multiplot
set output '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0_disp_vsys_z0.eps'
unset key
set xlabel 'Radius [arcsec]'
set xtics 200
set mxtics 2
set macros
TMARGIN = 'set tmargin at screen 0.94; set bmargin at screen 0.66; set lmargin at screen 0.10; set rmargin at screen 0.50'
MMARGIN = 'set tmargin at screen 0.66; set bmargin at screen 0.38; set lmargin at screen 0.10; set rmargin at screen 0.50'
BMARGIN = 'set tmargin at screen 0.38; set bmargin at screen 0.10; set lmargin at screen 0.10; set rmargin at screen 0.50'
set multiplot layout 3,1 rowsfirst
@LABELF
@TICSF
@TMARGIN
@NOXTICS
set yrange [0:112.79]
set ylabel '{/Symbol s} [km/s]'
set ytics 5
set mytics 5
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:4:($4+$15):($4+$16) w errorbars ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:4 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:4:($3+$15):($3+$16) w errorbars ls 2, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:4 w lp ls 2
@MMARGIN
@NOXTICS
set yrange [18.8131:45.216]
set ylabel 'V_{sys} [km/s]'
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:12:($12+$21):($12+$22) w errorbars ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:12 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:12 w lp ls 2
@BMARGIN
@XTICS
set xlabel 'Radius [arcsec]'
set yrange [0.0009:0.0011]
set ylabel 'Scale height [arcsec]'
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt'u 2:8 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:8 w lp ls 2
unset multiplot
set output '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0_xc_yc_cd.eps'
set multiplot layout 3,1 rowsfirst
@LABELF
@TICSF
@TMARGIN
@NOXTICS
set yrange [136.62:166.98]
set ylabel 'X_c [pix]'
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:10 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:10 w lp ls 2
@MMARGIN
@NOXTICS
set yrange [133.38:163.02]
set ylabel 'Y_c [pix]'
plot '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final1.txt' u 2:11 w lp ls 1, '/Users/francescarizzo/Documents/projects/CII_Dynamics_at_EoR/Raw_simulated_CII_cubes/serra_00_s23_h1842/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3/output/serra_00_snap_23_h1842_i_1.38_ca_2.9_4_2_3.alma_0.05arcsec_0/rings_final2.txt' u 2:11 w lp ls 2
unset multiplot; reset
