# analysis_backend.py - This files holds all of the graph and info generation
# Author: Julien Dhouti
# Data_Analysis : class - contains all of the attribute that the front end needs
#                       - includes graph + information generation
# Python 3.6.1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

class Data_Analysis:
    # this is where the file from the filepath gets transformed into a dataframe
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
        self.files = []

    def get_file_names(self):
        """Returns a list of all of the file names that were generated with each object."""
        return self.files

    def get_filepath(self):
        """Returns the file path of the given object."""
        return self.filepath

    def get_summary_statistics(self, *arg):
        """Create a summary of statistics for the given file using the describe
        method in the Pandas module. Takes in number of percentiles to return.
        Must be between 0 and 1!"""

        for percentile in arg:
            if percentile < 0 or percentile > 1:
                raise ValueError('Percentile must be between 0 and 1')
        return(self.data.describe(arg))

    def get_histogram(self, column, bins="missing", xaxis='X axis', yaxis='Y axis', title='Title'):
        """Return a generated histogram Image object and the string name of the file.

        Keyword arguments:
        column -- the name of the column the histogram should be generated from
        bins -- the amount of bins the user wants in the histogram (default auto generated)
        xaxis -- the name of the x label (default: 'X axis')
        yaxis -- the name of the y label (default: 'Y axis')
        title -- the title of the generated histogram (default: 'Title')
        """
        # check for any values that should not be accepted.
        if column not in self.data.columns:
            raise ValueError("Column cannot be found.")

        if bins == "missing":
            bins_not_given = True
        elif bins <= 0:
            raise ValueError("The amount of bins should be a positive number.")
        else:
            raise ValueError("User did not input a valud bins amount.")

        # generate the name of the histogram file
        while True:
            name = str(random.randint(1,10000)) + '.png'
            if name in self.files:  # check that the name hasn't already been assigned
                continue
            else:
                self.files.append(name)
                break

        # begin making the histogram
        values = self.data[column]  # values in the column you want to graph

        # if the user did not give any bins, let the .hist() function determine it
        if bins_not_given:
            plt.hist(values, ec='black')
        else:
            plt.hist(values, bins=bins, ec='black')

        plt.xlabel(xaxis)
        plt.title(title)
        plt.ylabel(yaxis)
        plt.savefig(name)

        img = Image.open(name)
        return img
