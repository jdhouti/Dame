# column_info.py - This files holds the class that contains information for each column
# Author: Julien Dhouti
# Column_Info : class - contains all of the attribute of each column in the given .csv file
# Python 3.6.1

import pandas as pd
import data_object as do

class Column(do.Data_Object):
    def __init__(self, series):
        """Will initialize the column info class by determining the kind of info
        inside of the given column.

        column: panda series -- contains all of the information in of the given column
        """

        self.series = series
        self.type = ""

        self.determined_type = False    # set to true if get_type was already run

    def get_column_name(self):
        return self.column

    def get_type(self):
        """Will return the data type as a string of a given panda series."""


        # checks to see if the type has already been determined to improve efficiency
        if self.determined_type:
            return self.type

        # if self.determined_type == false, type has not been determined so initiate
        # the analysis
        if 'int' in self.series.dtype or 'float' in self.series.dtype:
            self.type = 'numerical'
            self.determined_type = True
            return 'numerical'
        else:
            self.type = 'categorical'
            self.determined_type = True
            return 'categorical'
