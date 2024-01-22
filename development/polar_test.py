# Meant to test grid_mapping.py function-by-function with pre-determined polar coordinate data
# Note: have to restructure project so that this file can reference functions in src directory
import numpy as np
#from ..src import config as config
#from ..src import grid_mapping as gridmap
import sys


#Sample polar coordinates map
polar_map = {
    0: 10,    # 0 degrees, 10 units distance
    np.pi/4: 15,  # 45 degrees, 15 units distance
    np.pi/2: 20,  # 90 degrees, 20 units distance
    3*np.pi/4: 25,  # 135 degrees, 25 units distance
    np.pi: 30,  # 180 degrees, 30 units distance
    # ... and so on for other angles/distances
}

def flood_fill(blue_cells, pink_cells):
    # To be developed
    pass

if __name__ == "__main__":
    print (polar_map)
    # Will test functions here