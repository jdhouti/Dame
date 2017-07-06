# column_info.py - This files holds the class that contains information for each column
# Author: Julien Dhouti
# Column_Info : class - contains all of the attribute of each column in the given .csv file
# Python 3.6.1

import pandas as pd

class Column_Info:
    def __init__(self, path, column):
        """Will initialize the column info class by determining the kind of info
        inside of the given column.

        column: String -- contains all of the information in of the given column
        path: String -- the string that indicates the path to the csv file
        """
        data = pd.read_csv(path)
        try:
            self.column = data[column]
        except:
            raise ValueError("Column could not be found!")
        self.type = ""

    def get_type(self):
        """Will return the data type as a string of a given panda series."""
        if 'int' in str(self.column.dtype):
            self.type = 'int'
            return 'int'
        elif 'float' in str(self.column.dtype):
            self.type = 'float'
            return 'float'
        elif 'bool' in str(self.column.dtype):
            self.type = 'bool'
            return 'bool'
        elif 'string'
        else:
            self.type = 'mixed'
            return 'mixed'
