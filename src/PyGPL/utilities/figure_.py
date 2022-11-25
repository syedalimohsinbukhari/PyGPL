"""Created on Oct 16 22:48:20 2022."""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# taken from https://github.com/amithr/PySimpleGUI---Line-Graphs/blob/main/main-window.py
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# taken from https://stackoverflow.com/q/63155989
def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
