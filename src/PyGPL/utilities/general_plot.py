"""Created on Oct 29 16:27:01 2022."""

import PySimpleGUI as pSGUI

from .figure_ import delete_existing_figure, draw_new_figure
from .plotting_mechanics.GeneralPlot import GeneralPlot


def general_plot(plot_type):
    layout = [[pSGUI.Text(plot_type)],
              [pSGUI.Text('Input X'), pSGUI.InputText(key='-x-', expand_x=True), pSGUI.FileBrowse('Browse')],
              [pSGUI.Text('Input Y'), pSGUI.InputText(key='-y-', expand_x=True), pSGUI.FileBrowse('Browse')],
              [pSGUI.Text('x_label'), pSGUI.InputText(key='-x-label-', s=20),
               pSGUI.Text('y_label'), pSGUI.InputText(key='-y-label-', s=20),
               pSGUI.Text('color'), pSGUI.InputText(key='-color-', s=20),
               pSGUI.Text('title'), pSGUI.InputText(key='-title-', s=30)],
              [pSGUI.Button('Plot', key='-plot-'), pSGUI.Button('Plot & Save', key='-save-'),
               pSGUI.Button('Exit', key='-exit-')],
              [pSGUI.Canvas(key='-CANVAS-')]]

    win_ = pSGUI.Window(plot_type, layout=layout, size=(900, 600), auto_size_text=True, resizable=True, finalize=True)

    figure = None

    while True:
        event, values = win_.read()

        if event == pSGUI.WIN_CLOSED or event in ['-exit-', None]:
            break

        if event == '-plot-':
            figure = do_plot(fig=figure, plot_type=plot_type, values=values, win_=win_)

        if event == '-save-':
            figure = do_plot(fig=figure, plot_type=plot_type, values=values, win_=win_, save=True)

    win_.close()


def do_plot(fig, plot_type, values, win_, save=False):
    gp = GeneralPlot(pysimplegui_values=values)
    if fig is not None:
        delete_existing_figure(existing_figure=fig)

    return draw_new_figure(canvas_object=win_['-CANVAS-'].TKCanvas,
                           figure_object=gp.plot(plot_type=plot_type.lower(), save=save))
