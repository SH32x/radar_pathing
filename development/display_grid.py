# Intended to be standalone, does not require any other project files
# Visualizes 2 occupancy grids
# Can also test from terminal with "python -m development.display_grid"
from tkinter import *
import matplotlib.pyplot
from matplotlib.figure import Figure
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

grid_2 = [[0, 0, 0, 2, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0, 0]]

grid_3 = pt.generate_grid(pt.get_red_cells(pt.polar_map_s01)) #Test data

def update_gui():
    window.update_idletasks()
    window.update()

if __name__ == "__main__":
    # Init Tkinter GUI
    window = Tk()
    window.title('Grid Plotting Test')
    window.geometry("1600x800")

    # Init matplotlib figures
    fig = Figure(figsize=(16, 8), dpi=100)
    grid_plot_1 = fig.add_subplot(121)
    grid_plot_2 = fig.add_subplot(122)
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    # Draw the grids
    cmap_1 = matplotlib.colors.ListedColormap(['Blue', 'pink', 'red', 'purple'])
    canvas.draw()
    update_gui()
    grid_axis_1 = grid_plot_1.pcolor(grid_3[::-1], cmap=cmap_1, edgecolors='k', linewidths=3)
    grid_axis_2 = grid_plot_2.pcolor(grid_3[::-1], cmap=cmap_1, edgecolors='k', linewidths=3)
    canvas.draw()
    #canvas.create_line(80, 80, 500, 500)
    update_gui()
    window.mainloop()
    

