# scatter.py - This files contains the scatter object used to create a scatter object.
# Author: Julien Dhouti
# Scatter : class - contains all of the attribute to the scatter object
# Python 3.6.1
# /Users/Julien/Downloads

import graph
import numpy as np
import matplotlib.pyplot as plt
import file_name_generator as fng
from sklearn import datasets, linear_model

class Scatter(graph.Graph):
    """The scatter object represents a scatter plot."""

    def __init__(self, filepath):
        """Inits the Scatter object using the filepath.

        Args:
            filepath: a string specifying the filepath of where the file we want is located.
        """

        super().__init__(self, filepath)
        super().set_image(None)
        self.generator = fng.Name_Generator()

    def generate(self, column1, column2, ax, title=None, color=None):
        """Creates the scatter plot based on the two given columns.

        Args:
            column1: a string specifying the name of the first column to represent x axis.
            column2: a string specifying the name of the second column to represent the y axis.
            title: a string specifying the title of the graph.
            ax: a subplot on which the graph will be drawn on.

        Returns:
            An altered subplot object with a scatter plot graph that can be used in 
            the canvas method for the tkinter interface.
        """

        # Generates the name for the scatter plot.
        name = self.generator.generate_name(super().get_file_path(), column1, "scatter")
        super().set_image_name(name)

        # Adjust the color of the graph
        try:
            super().set_color(color)
        except ValueError:
            print("The given color is unavailable.")

        # Using the column name, strips the values from each column using pandas.
        col1values = self.data[column1]
        col2values = self.data[column2]
        
        ax.plot(col1values, col2values, 'ro', color=super().get_current_color())
        ax.set_xlabel(column1)
        ax.set_ylabel(column2)
        
        # If the title was given, it will be assigned to the figure.
        if title != None:
            ax.set_title(title)

        return ax

    def lin_generate(self, column1, column2, ax, title=None, color=None):
        """Generates a linear model. This is a regular scatter plot but with a
        linear regression line passing through it.

        Args:
            column1: a string specifying the name of the first column to represent x axis.
            column2: a string specifying the name of the second column to represent the y axis.
            title: a string specifying the title of the graph.
            ax: a subplot on which the graph will be drawn on.

        Returns:
            An altered subplot object with a linear line that can be used in 
            the canvas method for the tkinter interface.
        """
        # Adjust the color of the graph
        try:
            super().set_color(color)
        except ValueError:
            print("The given color is unavailable.")
        
        # Converts given columns into numpy arrays.
        column_x = super().get_data()[column1].values
        column_y = super().get_data()[column2].values

        # Creates the training model.
        m, b = np.polyfit(column_x, column_y, 1)

        ax.scatter(column_x, column_y,  color=super().get_current_color())
        ax.plot(column_x, m * column_x + b, '-')
        ax.set_xlabel(column1)
        ax.set_ylabel(column2)

        return ax