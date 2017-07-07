# histogram.py - This files contains the Graph object
# Author: Julien Dhouti
# Histogram : class - contains all of the attribute to the histogram object
# Python 3.6.1

import graph
import pandas as pd
from PIL import

class Histogram(Graph):
    def __init__(self, title):
        super().__init__("histogram", title)
        super().image = None

    def generate(self, column, units, bins=None):
        """Will generate the graph based on the given information."""
        # check for any values that should not be accepted. The column should be in the dataframe
        if column not in self.data.columns:
            raise ValueError("Column cannot be found.")

        if bins == None:   # bins will get initiated to "missing" in the parameter if not assigned a number.
            pass
        elif bins <= 0:
            raise ValueError("The amount of bins should be a positive number.")
        else:
            raise ValueError("User did not input a valid bins amount.")

        # generate the name of the histogram file
        name = generator.generate_name(self.filepath, column, "histogram")

        # ----------------------- begin making histogram ----------------------- #
        values = self.data[column]  # values in the column you want to graph
        # if the user did not give any bins, let the .hist() function determine it
        plt.figure()
        plt.hist(values, bins=bins, ec='black', color=super().currentColor)
        plt.xlabel(column)
        plt.ylabel(units)
        plt.title(title)
        plt.savefig(name)
        super().setImage(Image.open(name))
