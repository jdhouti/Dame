# scatter.py - This files contains the scatter object used to create a scatter object.
# Author: Julien Dhouti
# Scatter : class - contains all of the attribute to the scatter object
# Python 3.6.1

import Graph
import matplotlib.pyplot as plt
from PIL import Image
import file_name_generator as fng

class Scatter(Graph.graph):
    def __init__(self, title, data):
        super().__init__(self, title, data)
        super().setImage(None)
        generator = fng.Name_Generator()

    def generate(self, column1, column2):
        # check to see if the given columns actually exist in the csv file.
        if column1 not in super().getData.columns:
            raise ValueError(column1 + " cannot be found!")
        if column2 not in super().getData.columns:
            raise ValueError(column2 + " cannot be found!")
        if column2 == column1:
            raise ValueError("Both columns cannot be the same!")

        # generate the name for the scatter plot
        name = generator.generate_name(self.filepath, column1, "scatter")

        # using the column name, strip the values from each column using pandas
        col1values = self.data[column1]
        col2values = self.data[column2]

        # ----------------------- create the scatter plot ---------------------- #
        plt.figure()
        plt.plot(col1values, col2values, 'ro')
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.savefig(name)
        img = Image.open(name)
        return img
