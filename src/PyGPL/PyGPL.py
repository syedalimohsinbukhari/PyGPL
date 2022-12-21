"""Created on Sep 18 16:52:41 2022."""

import PySimpleGUI as pSGUI

from .utilities.general_plot import general_plot


def run():
    layout = [[pSGUI.Button('Line Plot', key='-line-plot-'),
               pSGUI.Button('Scatter Plot', key='-scatter-plot-'),
               pSGUI.Button('Bar Plot', key='-bar-plot-')],
              [pSGUI.Button('Exit', key='-exit-')]]

    root = pSGUI.Window('Main', layout, size=(900, 600), finalize=True)

    while True:
        event, values = root.read()

        if event == pSGUI.WIN_CLOSED or event in ['-exit-', None]:
            break

        if event == '-line-plot-':
            general_plot('Line Plot')

        if event == '-scatter-plot-':
            general_plot('Scatter Plot')

        elif event == '-bar-plot-':
            general_plot('Bar Plot')
    root.close()


if __name__ == '__main__':
    run()
