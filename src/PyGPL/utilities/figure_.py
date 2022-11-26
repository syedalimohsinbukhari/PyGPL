"""Created on Oct 16 22:48:20 2022."""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# taken from https://github.com/amithr/PySimpleGUI---Line-Graphs/blob/main/main-window.py
def draw_new_figure(canvas_object, figure_object):
    figure_canvas_agg = FigureCanvasTkAgg(figure_object, canvas_object)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# taken from https://stackoverflow.com/q/63155989
def delete_existing_figure(existing_figure):
    existing_figure.get_tk_widget().forget()
