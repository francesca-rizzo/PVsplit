import os
from pathlib import Path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_output_directory(current_directory):

    pvsplit_output_path = os.path.join(current_directory, 'pvsplit_output')
    pvsplit_output_directory = None
    if os.path.exists(pvsplit_output_path):
        pvsplit_output_directory = Path(pvsplit_output_path)
    else:
        os.mkdir(pvsplit_output_path)
        pvsplit_output_directory = Path(pvsplit_output_path)
    return pvsplit_output_directory

# Save the results to a text file
def write_to_text(p_major, p_minor1, p_minor2, p_v, p_r, pvsplit_output_directory):
    #Write to terminal
    print(f'P_major: {p_major}\n')
    print(f'P_minor1: {p_minor1}\n')
    print(f'P_minor2: {p_minor2}\n')
    print(f'P_v: {p_v}\n')
    print(f'P_r: {p_r}\n')

    output_text_path = os.path.join(pvsplit_output_directory, 'output.txt')
    
    with open(output_text_path, 'w') as f:
        f.write(f'P_major: {p_major}\n')
        f.write(f'P_minor1: {p_minor1}\n')
        f.write(f'P_minor2: {p_minor2}\n')
        f.write(f'P_v: {p_v}\n')
        f.write(f'P_r: {p_r}\n')

def plane_eq(p_major, p_v, p_r):
    # Generic plane equation with substitued values to find z intercept which is P_r
    a, b, c, d = -0.63, -0.27, 2.78, -2.72
    return (d - a*p_major - b*p_v) / c

# Draw 3D plots to show the results
def draw_3d_plots(p_major, p_v, p_r, pvsplit_output_directory):
    image_path = os.path.join(pvsplit_output_directory, '3d_plot.png')
    #Generate data for the plane
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = plane_eq(X, Y, p_r)

    # Create the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the plane
    ax.plot_surface(X, Y, Z, alpha=0.5)

    # Plot the point
    ax.scatter(p_major, p_v, p_r, color='r', s=100)

    a, b, c, d = -0.63, -0.27, 2.78, -2.72
    plane_value_at_point = a*p_major + b*p_v + c*p_r + d

    label = None
    if plane_value_at_point < 0:
        label = 'Disc'
    else:
        label = 'Not a disc'

    ax.text(p_major, p_v, p_r, label, color='black')

    # Set labels and title
    ax.set_xlabel('P_major')
    ax.set_ylabel('P_v')
    ax.set_zlabel('P_r')

    ax.view_init(9, -62)

    plt.savefig(image_path)

    plt.show()
    