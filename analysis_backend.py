# analysis_backend.py - This files holds all of the graph and info generation
# Author: Julien Dhouti
# Data_Analysis : class - contains all of the attribute that the front end needs
#                       - includes graph + information generation
# Python 3.6.1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data_Analysis:
    # this is where the file from the filepath gets transformed into a dataframe
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def get_summary_statistics(self, *arg):
        """Create a summary of statistics for the given file using the describe
        method in the Pandas module. Takes in number of percentiles to return.
        Must be between 0 and 1!"""

        for percentile in arg:
            if percentile < 0 or percentile > 1:
                raise ValueError('Percentile must be between 0 and 1')
        return(self.data.describe(arg))

    def get_histogram(self, column, bins=10, xaxis='X axis', yaxis='Y axis', title='Title'):
        # check for any values that should not be accepted.
        if column not in self.data.columns:
            raise ValueError("Column cannot be found.")
        if bins > 100:
            raise ValueError("You cannot have more than 100 bins.")

        # begin making the histogram
        values = self.data[column]  # values in the column you want to graph
        plt.hist(values, bins=bins)
        plt.xlabel(xaxis)
        plt.title(title)
        plt.ylabel(yaxis)
        plt.show()


obj1 = Data_Analysis("/Users/Julien/Downloads/FL_insurance_sample.csv")
print(obj1.get_summary_statistics())
obj1.get_histogram('policyID', 100)
