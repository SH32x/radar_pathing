========================
# Testing 'grid_mapping.py' =>
Since the display_grid.py file already lists data in cell form, the main functions that need to be ported over from grid_mapping.py are: bresenham(start, end), flood_fill(blue_cells, pink_cells), get_blue_cells(red_and_pink_cells), get_pink_cells(red_and_pink_cells, red_cells), and get_red_and_pink_cells(occupied_cells, angles)
===
Start with get_red_and_pink_cells, try and get the data list of all red cells given a multiarray grid.

Note: Polar maps look similar to the following:
polar_map = {
    0: 10,    # 0 degrees, 10 units distance
    np.pi/4: 15,  # 45 degrees, 15 units distance
    np.pi/2: 20,  # 90 degrees, 20 units distance
    3*np.pi/4: 25,  # 135 degrees, 25 units distance
    np.pi: 30,  # 180 degrees, 30 units distance
    # ... and so on for other angles/distances
}

Note 2: For the flood fill in the updated (harder) Bresenham algorithm the solution likely involves saving the coordinates for all vertices of every red cell then deciding which two of the four vertices per square will be targeted by the line based on what part of the grid the cells are relative to the center, there are 8 combinations based on position (NW, N, NE, E, SE, S, SW, W)

Between the polar map and occupancy grid, we would need some baseline representation of coordinates, polar->coord conversion and coord->cell conversion
Try looking into Kalmann filters in order to represent radar data accurately
========================
# polar_test.py Notes
Testing started at 2:15 PM, continued until 
function red_and_pink_cells is difficult to understand, it doesn't return anything relevant, only returns the red cells
whose cartesian and cell coordinates differ due to botched conversion
Actual Bresenham coordinate retrieval function format:
def get_bresenham(red cell array)
    -> Find the vertices of the red cells, and return them in a list