"""Created on Sep 18 15:21:41 2022."""

import matplotlib.pyplot as plt
from numpy import ndarray


class GeneralPlot:

    def __init__(self, pysimplegui_values):
        col = pysimplegui_values['-color-']

        self.x_label = pysimplegui_values['-x-label-']
        self.y_label = pysimplegui_values['-y-label-']
        self.title = pysimplegui_values['-title-']
        self.color = None if col == '' else col

        self.values = pysimplegui_values

        self.x = self.__get_value('-x-')
        self.y = self.__get_value('-y-')

        self.__consistency_check()

    def __get_value(self, variable):
        try:
            var = eval(self.values[variable])
            return [var] if not isinstance(var[0], list) else var
        except SyntaxError:
            exec(open(self.values[variable]).read(), data := {})
            var = data[list(data.keys())[-1]]
            return var.tolist() if isinstance(var, ndarray) else var

    def __consistency_check(self):
        len_x, len_y = len(self.x), len(self.y)

        if len_x < len_y:
            self.x = self.x * len_y
        elif len_y < len_x:
            self.y = self.y * len_x

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    def plot(self, plot_type, save=False):
        plt.clf()
        plt.close()

        if plot_type == 'line plot':
            plt.plot(self.x, self.y, color=self.color)
        elif plot_type == 'scatter plot':
            plt.scatter(self.x, self.y, color=self.color)

        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.tight_layout()

        if save:
            plt.savefig(f"{self.title.replace(' ', '_').upper()}.png")

        return plt.gcf()
