import numpy as np
import src.config as config

def polar_to_cart(r, theta):
    """Converts a set of polar data to cartesian coordinates"""
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y
def cart_to_cell(x, y):
    """Converts a set of cartesian coordinates to cell coordinates"""
    x_nearest_ind = find_nearest(config.cell_ranges, x)
    if x > config.cell_ranges[x_nearest_ind]:
        x_cell = int(x_nearest_ind - config.grid_size_internal / 2 + 0.5)
    else:
        x_cell = int(x_nearest_ind - config.grid_size_internal / 2 - 0.5)

    y_nearest_ind = find_nearest(config.cell_ranges, y)
    if y > config.cell_ranges[y_nearest_ind]:
        y_cell = int(y_nearest_ind - config.grid_size_internal / 2 + 0.5)
    else:
        y_cell = int(y_nearest_ind - config.grid_size_internal / 2 - 0.5)
    return x_cell, y_cell

def find_nearest(array, value):
    """Finds nearest cell to a given point on the gui"""
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

if __name__ == "__main__":
    '''Unused main function'''
    pass