# histogram.py - This files contains the histogram object used to build a histogram
# Author: Julien Dhouti
# Histogram : class - contains all of the attribute to the histogram object
# Python 3.6.1

import graph
from PIL import Image
import file_name_generator as fng
import matplotlib.pyplot as plt
import os

class Histogram(graph.Graph):
    def __init__(self, filepath):
        super().__init__("histogram", filepath)
        super().set_image(None)
        self.generator = fng.Name_Generator()

    def generate(self, column, bins=None, title=None, color='red'):
        """Will generate the graph based on the given information."""
        # check for any values that should not be accepted. The column should be in the dataframe
        if column not in super().get_data().columns:
            raise ValueError("Column cannot be found.")

        if bins == None:   # bins will get initiated to "missing" in the parameter if not assigned a number.
            pass
        elif bins <= 0:
            raise ValueError("The amount of bins should be a positive number.")

        # generate the name of the histogram file
        name = self.generator.generate_name(super().get_file_path(), column, "histogram")
        super().set_image_name(name)

        # ----------------------- begin making histogram ----------------------- #
        values = super().get_data()[column]  # values in the column you want to graph
        # if the user did not give any bins, let the .hist() function determine it
        plt.figure()
        if bins == None:
            plt.hist(values, ec='black', color=color)
        else:
            plt.hist(values, bins=bins, ec='black', color=color)
        plt.xlabel(column)
        plt.ylabel("Quantity")
        if title != None:
            plt.title(title)
        plt.savefig(name)
        super().set_image(Image.open(name))
        os.remove(name) # delete the file
