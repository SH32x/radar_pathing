"""This file was rushed and is not very well optimized, more work is necessary to clean it up"""

import numpy as np
import itertools
import config

def polar_to_cart(r, theta):
    """Converts a set of polar data to cartesian coordinates"""
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y
def cart_to_cell(x, y):
    """Converts a set of cartesian coordinates"""
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


def bresenham(start, end):
    """
    Implementation of Bresenham's line drawing algorithm
    See en.wikipedia.org/wiki/Bresenham's_line_algorithm
    Bresenham's Line Algorithm
    Produces a np.array from start and end (original from roguebasin.com)
    np.array([[4,4], [4,5], [5,6], [5,7], [5,8], [6,9], [6,10]])
    """
    # setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)  # determine how steep the line is
    if is_steep:  # rotate line
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    # swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1  # recalculate differentials
    dy = y2 - y1  # recalculate differentials
    error = int(dx / 2.0)  # calculate error
    y_step = 1 if y1 < y2 else -1
    # iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(int(x1), int(x2 + 1)):
        coord = [y, x] if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += y_step
            error += dx
    if swapped:  # reverse the list if the coordinates were swapped
        points.reverse()
    points = np.array(points)
    return points


def flood_fill(blue_cells, pink_cells):
    """Yet to be implemented"""
    pass

def get_blue_cells(red_and_pink_cells):
    """Given a list of red and pink cells, returns a list of the remaining unoccupied cells"""
    blue_cells = []
    for x in range(config.grid_size):
        x = x - (config.grid_size - 1)/2
        for y in range(config.grid_size):

            y = y - (config.grid_size - 1)/2
            if [x, y] not in red_and_pink_cells:
                blue_cells.append([x,y])

    for cell in blue_cells:
        if cell in red_and_pink_cells:
            print("ERROR")

    return blue_cells

def get_pink_cells(red_and_pink_cells, red_cells):
    """Given a list of red and pinks cells, and another list of just red cells, returns a list of just pink cells"""
    pink_cells = []
    red_cells = [list(ele) for ele in red_cells]
    for cell in red_and_pink_cells:
        if cell not in red_cells:
            pink_cells.append(cell)

    for cell in pink_cells:
        if cell in red_cells:
            print("ERROR")

    return pink_cells


# Find cells behind occupied cells
# Method 1:
def get_red_and_pink_cells(occupied_cells, angles):
    """Given the red cells, returns a list of red and pink cells"""
    red_and_pink_cells = []
    for i, occupied_cell in enumerate(occupied_cells):

        angle = angles[i]

        x, y = (polar_to_cart(np.sqrt(2) * config.max_range, angle))
        distant_cell = cart_to_cell(x,y)
        print(occupied_cell)
        print(distant_cell)
        if distant_cell != occupied_cell:
            print(f"Occupied Cell: {occupied_cell}")
            print(f"Angle: {np.degrees(angle)}")
            print(f"Distant Cell: {distant_cell}")

            m = bresenham(occupied_cell, distant_cell).tolist()
            print(f"Marked Cells: {str(m)}")
        for k in m:
            red_and_pink_cells.append(k)

    # Flood Fill
    pink_cells = get_pink_cells(red_and_pink_cells, occupied_cells)

    for k in range(5): # number of iterations
        blue_cells, pink_cells = flood_fill(get_blue_cells(red_and_pink_cells), pink_cells)

        for (x,y) in occupied_cells:
            if [x, y] in pink_cells:
                pink_cells.pop(pink_cells.index([x,y]))

        print(red_and_pink_cells)
        red_and_pink_cells = pink_cells
        for j in occupied_cells:
            red_and_pink_cells.append([j[0], j[1]])

        for x,y in occupied_cells:
            if [x, y] in pink_cells:
                pink_cells.pop(pink_cells.index([x,y]))

    return red_and_pink_cells

def cell_to_grid_representation(cell):
    y = int((cell[1] + config.grid_size / 2) - 0.5)
    x = int(cell[0] + config.grid_size / 2 - 0.5)
    return x,y


def main(polar_map):
    angles = list(polar_map.keys())
    distances = list(polar_map.values())
    print(angles)
    print(distances)
    # Convert polar to cartesian (add the max range to convert to an absolute value grid where the vehicle is centered)
    y_cart = distances * np.sin(angles)
    x_cart = distances * np.cos(angles)

    print(f"xcart {x_cart}")
    occupied_cells = []
    # Find occupied cells
    for index, x in enumerate(x_cart):
        y = y_cart[index]
        x_cell, y_cell = cart_to_cell(x,y)
        occupied_cells.append((x_cell, y_cell))

    new_occupied_cells = []
    new_angles = []
    for i, cell in enumerate(occupied_cells):
        if cell not in new_occupied_cells:
            new_occupied_cells.append(cell)
            new_angles.append(angles[i])

    angles = new_angles
    occupied_cells = new_occupied_cells

    occupied_cells = list(dict.fromkeys(occupied_cells))  # remove dupes

    print(f"Occupied cells: {occupied_cells}")
    red_and_pink_cells = get_red_and_pink_cells(occupied_cells, angles)


    grid = np.zeros((config.grid_size, config.grid_size))
    red_and_pink_cells.sort()
    red_and_pink_cells = list(red_cells for red_cells, _ in itertools.groupby(red_and_pink_cells)) # Remove dupes
    for x,y in occupied_cells:
        red_and_pink_cells.append([x,y])
    print(f"Red and Pink Cells: {red_and_pink_cells}")
    pink_cells = get_pink_cells(red_and_pink_cells, occupied_cells)

    for i, cell in enumerate(red_and_pink_cells):

        x = cell[0]
        y = cell[1]

        if [x, y] in pink_cells:

            grid[int(-(y + config.grid_size / 2) - 0.5), int(x + config.grid_size / 2 - 0.5)] = 1
        if (x, y) in occupied_cells:
            print([x,y])
            grid[int(-(y + config.grid_size/2) - 0.5), int(x + config.grid_size/2 - 0.5)] = 2

    return grid











