# column_info.py - This files holds the class that contains information for each column
# Author: Julien Dhouti
# Column_Info : class - contains all of the attribute of each column in the given .csv file
# Python 3.6.1

import pandas as pd

class Column:
    def __init__(self, column):
        """Will initialize the column info class by determining the kind of info
        inside of the given column.

        column: String -- contains all of the information in of the given column
        path: String -- the string that indicates the path to the csv file
        """


        self.column = column
        self.type = ""
        self.determined_type = False    # set to true if get_type was already run

    def get_type(self):
        """Will return the data type as a string of a given panda series."""


        # checks to see if the type has already been determined to improve efficiency
        if self.determined_type:
            return self.type

        # if self.determined_type == false, type has not been determined so initiate
        # the analysis
        if 'int' in str(self.column.dtype) or 'float' in str(self.column.dtype):
            self.type = 'numerical'
            self.determined_type = True
            return 'numerical'
        else:
            self.type = 'categorical'
            self.determined_type = True
            return 'categorical'
