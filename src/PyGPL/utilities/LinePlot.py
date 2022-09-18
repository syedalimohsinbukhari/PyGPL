"""Created on Sep 18 15:21:41 2022."""

import matplotlib.pyplot as plt


class LinePlot:

    def __init__(self, pysimplegui_values):
        x = eval(pysimplegui_values['-x-'])
        self.x = [x] if not isinstance(x[0], list) else x

        y = eval(pysimplegui_values['-y-'])
        self.y = [y] if not isinstance(y[0], list) else y

        col = pysimplegui_values['-color-']

        self.x_label = pysimplegui_values['-x-label-']
        self.y_label = pysimplegui_values['-y-label-']
        self.title = pysimplegui_values['-title-']
        self.color = None if col == '' else col

        self.__consistency_check()

    @staticmethod
    def __strip(val):
        return [float(i) for i in val.replace('[', '').replace(']', '').split(',')]

    def __consistency_check(self):
        len_x, len_y = len(self.x), len(self.y)

        if len_x < len_y:
            self.x = self.x * len_y

        if len_y < len_x:
            self.y = self.y * len_x

    def plot(self, save=False):
        plt.clf()
        plt.close()

        [plt.plot(i, j, color=self.color) for i, j in zip(self.x, self.y)]

        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)

        plt.tight_layout()

        if save:
            plt.savefig(f'{self.title}.png')

        return plt.gcf()
