# Intended to be standalone, does not require any other project files
# Visualizes 2 occupancy grids
# Can also test from terminal with "python -m development.display_grid"
from tkinter import *
import matplotlib.pyplot
import numpy as np
from src import config as config
from src import coords as coords
from matplotlib.figure import Figure
import matplotlib.lines as lines
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import time
from development import polar_test as pt


grid_1 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

grid_2 = [[0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 2, 2, 2, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0]]

red = pt.get_red_cells(pt.polar_map_s01)
grid_3 = pt.generate_grid(red) #Test data

def update_gui():
    window.update_idletasks()
    window.update()


def classify_cell_location(cell):
    x, y = pt.cell_to_grid_representation(cell)
    # cx, cy = pt.cell_to_grid_representation(center)
    cx = int(ctr[0])
    cy = int(ctr[1])
    print("Next cell")
    print(f"Center: {cx}, {cy}")
    print(f"Cell: {x}, {y}")
    print(" ")

    return {
        (x < cx and y > cy): [0, 0, 2, 2],  # top left
        (x == cx and y > cy): [0, 0, 2, 0],  # top center
        (x > cx and y > cy): [0, 2, 2, 0],  # top right
        (x < cx and y == cy): [2, 2, 2, 0],  # middle left
        (x == cx and y == cy): [0, 0, 0, 0],  # center
        (x > cx and y == cy): [0, 0, 0, 2],  # middle right
        (x < cx and y < cy): [0, 2, 2, 0],  # bottom left
        (x == cx and y < cy): [2, 2, 0, 2],  # bottom center 
        (x > cx and y < cy): [0, 0, 2, 2],  # bottom right
    }[True]


if __name__ == "__main__":
    # Init Tkinter GUI
    window = Tk()
    window.title("Grid Plotting Test")
    window.geometry("1600x800")

    # Init matplotlib figures
    fig = Figure(figsize=(16, 8), dpi=100)
    grid_plot_1 = fig.add_subplot(121)
    grid_plot_2 = fig.add_subplot(122)
    canvas = FigureCanvasTkAgg(fig, master=window)
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    # Draw the grids
    cmap_1 = matplotlib.colors.ListedColormap(["Blue", "pink", "red", "purple"])
    canvas.draw()
    update_gui()
    grid_axis_1 = grid_plot_1.pcolor(
        grid_3[::-1], cmap=cmap_1, edgecolors="k", linewidths=3
    )
    grid_axis_2 = grid_plot_2.pcolor(
        grid_3[::-1], cmap=cmap_1, edgecolors="k", linewidths=3
    )
    canvas.draw()

    # Assuming `grid_plot_1` is your Axes object

    x_range = grid_plot_1.get_xlim()
    y_range = grid_plot_1.get_ylim()
    #print(f"X-axis range: {x_range}")
    #print(f"Y-axis range: {y_range}")

    # Draw the lines
    ctr = ((config.grid_size - 1) / 2 + config.cell_size), (
        (config.grid_size - 1) / 2 + config.cell_size
    )
    # Template: grid_plot_1.plot([X, ctr[0]], [Y, ctr[1]], color='yellow')
    # print(red)

    # This below part is necessary to prevent the margins of the plot from being extended
    """
    The additional white space is likely being added because the plot function in Matplotlib automatically adjusts the 
    limits of the x-axis and y-axis to include all data points. When you add config.cell_size * 2 to x and y, you're 
    effectively moving the end point of the line outside the original grid. Matplotlib then expands the axes to 
    accommodate this new point, which results in additional white space.
    """
    x_lim = grid_plot_1.get_xlim()
    y_lim = grid_plot_1.get_ylim()

    for i, cell in enumerate(red):
        x, y = pt.cell_to_grid_representation(cell)
        dir = classify_cell_location(cell)

        grid_plot_1.plot(
            [x + (config.cell_size * dir[0]), ctr[0]],
            [y + (config.cell_size * dir[1]), ctr[1]],
            color="yellow",
        )
        grid_plot_1.plot(
            [x + (config.cell_size * dir[2]), ctr[0]],
            [y + (config.cell_size * dir[3]), ctr[1]],
            color="yellow",
        )
        grid_plot_2.plot([x, ctr[0]], [y, ctr[1]], color="yellow")
        # Note: Base is bottom left corner
        #print(x, y)

    # Reset the limits
    grid_plot_1.set_xlim(x_lim)
    grid_plot_1.set_ylim(y_lim)

    canvas.draw()
    update_gui()
    window.mainloop()
