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

<<<<<<< HEAD
    def get_column_name(self):
        return self.column

=======

    def get_name(self):
        return self.column
>>>>>>> a9547b417a4061f2b8502a68e5fe24b47de11a05
    def get_type(self):
        """Will return the data type as a string of a given panda series."""


        # checks to see if the type has already been determined to improve efficiency
        if self.determined_type:
            return self.type

        # if self.determined_type == false, type has not been determined so initiate
        # the analysis
<<<<<<< HEAD
        if 'int' in self.series.dtype or 'float' in self.series.dtype:
=======
        # if 'int' in self.column.dtype or 'float' in self.column.dtype:
        if True:
>>>>>>> a9547b417a4061f2b8502a68e5fe24b47de11a05
            self.type = 'numerical'
            self.determined_type = True
            return 'numerical'
        else:
            self.type = 'categorical'
            self.determined_type = True
            return 'categorical'
