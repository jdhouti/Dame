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
import file_name_generator as fng

generator = fng.Name_Generator()

class Data_Object:
    """This is the master object."""
    # this is where the file from the filepath gets transformed into a dataframe
    def __init__(self, filepath):
        self.filepath = filepath
        # this will continue working as long as the only permitted files are .csv files.
        self.data = pd.read_csv(filepath)

    def get_data(self):
        return self.data

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
