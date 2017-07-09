# analysis_backend.py - This files holds all of the graph and info generation
# Author: Julien Dhouti
# Data_Analysis : class - contains all of the attribute that the front end needs
#                       - includes graph + information generation
# Python 3.6.1

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# ---------------------------------
# This is some weird shenanigans but Stack Overflow said it worked
# And it does lmao
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
# -------------------------------------
from PIL import Image
import random
import file_name_generator as fng

generator = fng.Name_Generator()

class Data_Analysis:
    # this is where the file from the filepath gets transformed into a dataframe
    def __init__(self, filepath):
        self.filepath = filepath
        # this will continue working as long as the only permitted files are .csv files.
        self.data = pd.read_csv(filepath)

    def get_columns(self):
        """Returns list of all of the columns in the given .csv file."""
        return list(self.data.columns)

    def get_filepath(self):
        """Returns the file path of the given object."""
        return self.filepath

    def get_summary_statistics(self, *arg):
        """Create a summary of statistics for the given file using the describe
        method in the Pandas module. Takes in number of percentiles to return.
        Must be between 0 and 1!"""

        for percentile in arg:
            # the .describe() method only accepts numbers between 0 and 1 for percentages
            if percentile < 0 or percentile > 1:
                raise ValueError('Percentile must be between 0 and 1')
        return(self.data.describe(arg))

    def get_histogram(self, column, bins=None, title='Title'):
        """Return a generated histogram Image object

        Keyword arguments:
        column: String -- the name of the column the histogram should be generated from
        units: String -- the units for the y axis
        bins: int -- the amount of bins the user wants in the histogram (default auto generated)
        title: String -- the title of the generated histogram (default: 'Title')
        """
        # check for any values that should not be accepted. The column should be in the dataframe
        if column not in self.data.columns:
            raise ValueError("Column cannot be found.")

        if not bins:   # bins will get initiated to "missing" in the parameter if not assigned a number.
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
        plt.hist(values, bins=bins, ec='black')
        plt.xlabel(column)
        plt.ylabel("Quantity")
        plt.title(title)
        plt.savefig(name)
        img = Image.open(name)
        return img

    def get_scatter_plot(self, column1, column2, title='Title'):
        """Returns a generated scatter plot Image object

        Keyword arguments:
        column1 -- the name of the first column. Goes on the x axis
        column2 -- the name of the second column. Goes on the y axis
        xaxis -- the x axis label
        yaxis -- the y axis label
        title -- the title of the graph
        """
        # check to see if the given columns actually exist in the csv file.
        if column1 not in self.data.columns:
            raise ValueError(column1 + " cannot be found!")
        if column2 not in self.data.columns:
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
