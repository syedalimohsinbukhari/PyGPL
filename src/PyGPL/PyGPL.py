"""Created on Sep 18 16:52:41 2022."""

import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utilities.LinePlot import LinePlot


# taken from https://github.com/amithr/PySimpleGUI---Line-Graphs/blob/main/main-window.py
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# taken from https://stackoverflow.com/q/63155989
def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()


def run():
    layout = [[sg.Text('LinePlot')],
              [sg.Text('Input X'), sg.InputText(key='-x-', expand_x=True), sg.FileBrowse('Browse')],
              [sg.Text('Input Y'), sg.InputText(key='-y-', expand_x=True), sg.FileBrowse('Browse')],
              [sg.Text('x_label'), sg.InputText(key='-x-label-', s=15),
               sg.Text('y_label'), sg.InputText(key='-y-label-', s=15),
               sg.Text('color'), sg.InputText(key='-color-', s=15), sg.Text('title'), sg.InputText(key='-title-', s=30),
               sg.Button('Save')],
              [sg.Button('Plot'), sg.Button('Exit')],
              [sg.Canvas(key='-CANVAS-')]]

    root = sg.Window('PyGPL Interface', layout=layout, size=(900, 900), auto_size_text=True, resizable=True)

    fig_agg = None

    while True:
        event, values = root.read()
        lp = LinePlot(pysimplegui_values=values)
        save = True if event == 'Save' else False

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

        if fig_agg is not None:
            delete_fig_agg(fig_agg=fig_agg)

        fig_agg = draw_figure(root['-CANVAS-'].TKCanvas, lp.plot(save=save))

    root.close()


if __name__ == '__main__':
    run()
