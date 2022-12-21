"""Created on Sep 18 15:21:41 2022."""

import importlib.util

import matplotlib.pyplot as plt
import numpy as np


class GeneralPlot:

    def __init__(self, pysimplegui_values):
        col = pysimplegui_values['-color-']

        self.x_label = pysimplegui_values['-x-label-']
        self.y_label = pysimplegui_values['-y-label-']
        self.title = pysimplegui_values['-title-']
        self.color = None if col == '' else col

        self.values = pysimplegui_values

        self.x = np.array(self.__get_value('-x-'))
        self.y = np.array(self.__get_value('-y-'))

        self.__consistency_check()

    def __get_value(self, variable):
        try:
            return eval(self.values[variable])
        except SyntaxError:
            spec = importlib.util.spec_from_file_location("data", self.values[variable])
            data_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(data_module)
            return data_module.__dict__[list(data_module.__dict__.keys())[-1]]

    def __consistency_check(self):
        len_x, len_y = len(self.x), len(self.y)
        if len_x < len_y:
            self.x = np.pad(self.x, (0, len_y - len_x), 'constant')
        elif len_y < len_x:
            self.y = np.pad(self.y, (0, len_x - len_y), 'constant')

    def plot(self, plot_type, save=False):
        plt.clf()
        plt.close()

        if plot_type != 'bar plot':
            plt.grid('on')

        plot_functions = {
            'line plot': plt.plot,
            'scatter plot': plt.scatter,
            'bar plot': plt.bar
            }
        plot_functions[plot_type](self.x, self.y, color=self.color)

        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.tight_layout()

        if save:
            plt.savefig(f"{self.title.replace(' ', '_').upper()}.png")

        return plt.gcf()
