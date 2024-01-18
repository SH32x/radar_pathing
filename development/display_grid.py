# Intended to be standalone, does not require any other project files
# Visualizes 2 occupancy grids
from tkinter import *
import matplotlib.pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import time


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
    cmap_1 = matplotlib.colors.ListedColormap(['Blue', 'red', 'pink', 'purple'])
    canvas.draw()
    update_gui()
    grid_axis_1 = grid_plot_1.pcolor(grid_1[::-1], cmap=cmap_1, edgecolors='k', linewidths=3)
    grid_axis_2 = grid_plot_2.pcolor(grid_2[::-1], cmap=cmap_1, edgecolors='k', linewidths=3)
    canvas.draw()
    update_gui()
    window.mainloop()

