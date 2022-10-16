"""Created on Sep 18 16:52:41 2022."""

import PySimpleGUI as pSGUI
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


def line_plot():
    layout = [[pSGUI.Text('LinePlot')],
              [pSGUI.Text('Input X'), pSGUI.InputText(key='-x-', expand_x=True), pSGUI.FileBrowse('Browse')],
              [pSGUI.Text('Input Y'), pSGUI.InputText(key='-y-', expand_x=True), pSGUI.FileBrowse('Browse')],
              [pSGUI.Text('x_label'), pSGUI.InputText(key='-x-label-', s=15),
               pSGUI.Text('y_label'), pSGUI.InputText(key='-y-label-', s=15),
               pSGUI.Text('color'), pSGUI.InputText(key='-color-', s=15),
               pSGUI.Text('title'), pSGUI.InputText(key='-title-', s=30),
               pSGUI.Button('Save', key='-save-')],
              [pSGUI.Button('Plot', key='-plot-'), pSGUI.Button('Exit', key='-exit-')],
              [pSGUI.Canvas(key='-CANVAS-')]]

    win_lp = pSGUI.Window('Line Plot', layout=layout, size=(900, 600), auto_size_text=True, resizable=True,
                          finalize=True)

    fig_agg = None

    while True:
        event, values = win_lp.read()

        if event == pSGUI.WIN_CLOSED or event in ['-exit-', None]:
            break

        if event == '-plot-':
            lp = LinePlot(pysimplegui_values=values)
            save = True if event == '-save-' else False

            if fig_agg is not None:
                delete_fig_agg(fig_agg=fig_agg)

            fig_agg = draw_figure(win_lp['-CANVAS-'].TKCanvas, lp.plot(save=save))

    win_lp.close()


def run():
    layout = [[pSGUI.Button('Line Plot', key='-line-plot-')],
              [pSGUI.Button('Exit', key='-exit-')]]

    root = pSGUI.Window('Main', layout, finalize=True)

    while True:
        event, values = root.read()

        if event == pSGUI.WIN_CLOSED or event in ['-exit-', None]:
            break

        if event == '-line-plot-':
            line_plot()

    root.close()


if __name__ == '__main__':
    run()
