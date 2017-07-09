# scatter.py - This files contains the scatter object used to create a scatter object.
# Author: Julien Dhouti
# Scatter : class - contains all of the attribute to the scatter object
# Python 3.6.1

import graph
import matplotlib.pyplot as plt
from PIL import Image
import file_name_generator as fng
import os

class Scatter(graph.Graph):
    def __init__(self, filepath):
        super().__init__(self, filepath)
        super().set_image(None)
        self.generator = fng.Name_Generator()

    def generate(self, column1, column2, title=None, color='red'):
        # check to see if the given columns actually exist in the csv file.
        if column1 not in super().getData().columns:
            raise ValueError(column1 + " cannot be found!")
        if column2 not in super().getData().columns:
            raise ValueError(column2 + " cannot be found!")
        if column2 == column1:
            raise ValueError("Both columns cannot be the same!")

        super().changeColor(color) # set the color of the graph based on the color that was given

        # generate the name for the scatter plot
        name = self.generator.generate_name(super().getFilePath(), column1, "scatter")
        super().setImageName(name)  # send that name to the graph object

        # using the column name, strip the values from each column using pandas
        col1values = self.data[column1]
        col2values = self.data[column2]

        # ----------------------- create the scatter plot ---------------------- #
        plt.figure()
        plt.plot(col1values, col2values, 'ro', color=color)
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.savefig(name)
        if title != None:
            plt.title(title)
        super().setImage(Image.open(name))  # update the self.image of the graph by giving it a img object
        os.remove(name) # remove the image once we're done with it
