-THIS FILE CONTAINS PAIRS OF OCCUPANCY GRIDS, ONE BEFORE THE FLOOD FILL, AND ONE AFTER

-THE GOAL OF THE FLOOD FILL IS TO MARK ANY CELLS BEHIND A DETECTED OBJECT AS POTENTIALLY OCCUPIED

-USING THE display_grid.py FILE, THE GRIDS BELOW CAN BE VISUALIZED, (BLUE = UNOCCUPIED, RED = OCCUPIED, PINK = POTENTIALLY OCCUPIED, PURPLE = VEHICLE LOCATION)

-FOR THE SAKE OF SIMPLICITY, THE GRID SIZE WILL ALWAYS BE SQUARE AND ODD (ALLOWING US TO ASSUME THE VEHICLE IS IN THE CENTER OF THE GRID)

-THE FLOOD FILLED GRIDS DO NOT NEED TO PERFECTLY MATCH THE DESIRED TEST RESULT, IT CAN BE A LITTLE OFF


TEST GRIDS:
===========
1 - Simple Small Grid

Input (before flood fill):

grid_1 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

Output (after flood fill):

grid_2 = [[0, 0, 0, 2, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0, 0]]