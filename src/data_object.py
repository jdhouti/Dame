# analysis_backend.py - This files holds all of the graph and info generation
# Author: Julien Dhouti
# Data_Analysis : class - contains all of the attribute that the front end needs
#                       - includes graph + information generation
# Python 3.6.1

import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image
import file_name_generator as fng
generator = fng.Name_Generator()

class Data_Object:
    def __init__(self, filepath):
        self.filepath = filepath
        # this will continue working as long as the only permitted files are .csv files.
        self.data = pd.read_csv(filepath)

    def get_data(self):
        """Returns the data as a panda series."""
        return self.data

    def get_num_columns(self):
        """Will return the data type as a string of a given panda series."""

        num_cols = []
        for col in self.data.columns:
            if 'int' in str(self.data[col].dtype) or 'float' in str(self.data[col].dtype):
                num_cols.append(col)

        return num_cols


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
        return self.data.describe(arg)
