
# Meant to test grid_mapping.py function-by-function with pre-determined polar coordinate data
# Note: have to restructure project so that this file can reference functions in src directory
import numpy as np
from src import config as config
from src import coords as coords
from src import grid_mapping as gridmap


#Sample polar coordinates map
polar_map_s01 = {
    0: 10,    # 0 degrees, 10 units distance
    np.pi/4: 15,  # 45 degrees, 15 units distance
    np.pi/2: 20,  # 90 degrees, 20 units distance
    3*np.pi/4: 25,  # 135 degrees, 25 units distance
    np.pi: 30,  # 180 degrees, 30 units distance
    5*np.pi/4: 35,  # 225 degrees, 35 units distance
    3*np.pi/2: 40,  # 270 degrees, 40 units distance
    7*np.pi/4: 45  # 315 degrees, 45 units distance
}

def flood_fill(blue_cells, pink_cells):
    # To be developed
    pass

def get_red_cells(polar_map):
    '''
    Given a polar coordinate map, return an array of the occupied cells in the map (red cells)
    Currently works properly, ex. input polar_map_s01 returns [(10, 0), (10, 10), (0, 10), (-10, 10), (-10, 0),
    (-10, -10), (0, -10), (10, -10)] equal in length to the array angles[]
    '''
    angles = list(polar_map.keys())
    distances = list(polar_map.values())
    #print(angles)
    #print(distances)
    # Convert polar to cartesian (add the max range to convert to an absolute value grid where the vehicle is centered)
    y_cart = distances * np.sin(angles)
    x_cart = distances * np.cos(angles)

    #print(f"xcart {x_cart}")
    red_cells = []
    # Find red cells
    for index, x in enumerate(x_cart):
        y = y_cart[index]
        x_cell, y_cell = coords.cart_to_cell(x,y)
        red_cells.append((x_cell, y_cell))

    new_red_cells = []
    new_angles = []
    for i, cell in enumerate(red_cells):
        if cell not in new_red_cells:
            new_red_cells.append(cell)
            new_angles.append(angles[i])

    angles = new_angles
    red_cells = new_red_cells
    red_cells = list(dict.fromkeys(red_cells))  # remove dupes

    return red_cells

def generate_grid():
    grid = np.zeros((config.grid_size, config.grid_size))

def bresenham(start, end):
    """
    Implementation of Bresenham's line drawing algorithm
    See en.wikipedia.org/wiki/Bresenham's_line_algorithm
    Bresenham's Line Algorithm
    Input parameter format is ((cartesian pair), (cell pair))
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

def get_bresenham(red_cells, angles):
    '''
    Given the red cells and polar coordinate angles, return a list of marked red cells
    Note: After testing, I'm not quite sure what the relevance of the marked cells are,
    it appears to cover only those cells whose cartesian and cell coordinates differ
    '''
    red_and_pink_cells = []
    m = []
    for i, occupied_cell in enumerate(red_cells):
        angle = angles[i]
        x, y = (coords.polar_to_cart(np.sqrt(2) * config.max_range, angle))
        distant_cell = coords.cart_to_cell(x,y)
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
            
if __name__ == "__main__":
    # Will test functions here
    angles = list(polar_map_s01.keys())
    r = get_red_cells(polar_map_s01)
    #print (polar_map_s01)
    #print (angles)
    #print (r)
    red_and_pink_cells = []
    m = []
    for i, occupied_cell in enumerate(r):
        '''
        How I tested this function: I recreated it piece by piece and had it print variable outputs at each step
        '''
        angle = angles[i]
        x, y = (coords.polar_to_cart(np.sqrt(2) * config.max_range, angle))
        #print ('x = ', x)
        #print ('y = ', y)
        #print ('angle', i, 'is', angles[i])
        distant_cell = coords.cart_to_cell(x,y)
        if distant_cell != occupied_cell:
            m = bresenham(occupied_cell, distant_cell).tolist()
            print(f"Marked Cells: {str(m)}")
        for k in m:
            red_and_pink_cells.append(k) #Note: The error was in this line, m had not been previously defined
    print(f"Red Cells: {str(r)}")
    
    
    '''
    Test function comment block
    def line_draw (points):
    # Given an array of Bresenham points and the origin, draw lines from the origin to the points
    # Input format: np.array([[4,4], [4,5], [5,6], [5,7], [5,8], [6,9], [6,10]])
    # Make sure the lines pass through the corners of the cells, not the centers
    
    '''