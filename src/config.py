import numpy as np

max_range = 5
grid_range = 2*max_range
grid_size = 21 # nxn, must be odd
grid_size_internal = grid_size - 2
grid_center = (int((grid_size - 1)/2), int((grid_size - 1)/2))
cell_size = 2 * max_range / grid_size_internal
# Generate lists of cell ranges
cell_ranges = np.linspace(-max_range, max_range, grid_size_internal + 1)