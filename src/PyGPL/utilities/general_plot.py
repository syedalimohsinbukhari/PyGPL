"""Created on Oct 29 16:27:01 2022."""

import PySimpleGUI as pSGUI

from .figure_ import delete_fig_agg, draw_figure
from .plotting_mechanics.GeneralPlot import GeneralPlot


def general_plot(plot_type):
    show_x = pSGUI.Text()
    show_y = pSGUI.Text()

    layout = [[pSGUI.Text(plot_type)],
              [pSGUI.Text('Input X'), pSGUI.InputText(key='-x-', expand_x=True), pSGUI.FileBrowse('Browse')],
              [pSGUI.Text('Input Y'), pSGUI.InputText(key='-y-', expand_x=True), pSGUI.FileBrowse('Browse')],
              [pSGUI.Text('x_label'), pSGUI.InputText(key='-x-label-', s=20),
               pSGUI.Text('y_label'), pSGUI.InputText(key='-y-label-', s=20),
               pSGUI.Text('color'), pSGUI.InputText(key='-color-', s=20),
               pSGUI.Text('title'), pSGUI.InputText(key='-title-', s=30)],
              [pSGUI.Button('Show X', key='-show-x-'), pSGUI.Button('Show Y', key='-show-y-'),
               pSGUI.Button('Plot', key='-plot-'), pSGUI.Button('Plot & Save', key='-save-'),
               pSGUI.Button('Exit', key='-exit-')],
              [pSGUI.Text('X'), show_x, pSGUI.Text('Y'), show_y],
              [pSGUI.Canvas(key='-CANVAS-')]]

    win_ = pSGUI.Window(plot_type, layout=layout, size=(900, 600), auto_size_text=True, resizable=True,
                        finalize=True)

    fig_agg = None

    while True:
        event, values = win_.read()

        if event == pSGUI.WIN_CLOSED or event in ['-exit-', None]:
            break

        if event == '-plot-':
            fig_agg = plot_or_save(fig_agg, plot_type, values, win_)

        if event == '-save-':
            fig_agg = plot_or_save(fig_agg, plot_type, values, win_, True)

        if event == '-show-x-':
            show_x.update(GeneralPlot(values).get_x)
        elif event == '-show-y-':
            show_y.update(GeneralPlot(values).get_y)

    win_.close()


def plot_or_save(fig_agg, plot_type, values, win_, save=False):
    gp = GeneralPlot(pysimplegui_values=values)
    if fig_agg is not None:
        delete_fig_agg(fig_agg=fig_agg)

    return draw_figure(win_['-CANVAS-'].TKCanvas, gp.plot(save=save, plot_type=plot_type.lower()))
