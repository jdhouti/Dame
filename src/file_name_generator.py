# generator.py - This file contains the functions that generate the names for the
# files generated in the data_analysis.py file.
# Author: Julien Dhouti

import random

class Name_Generator:
    def generate_name(self, filepath, column):
        """Generates a name for a given filepath

        filepath: String -- the filepath of the file needing a name
        column: String -- the first column or keyword associated with the file
        """
        name, counter = "", -1
        while True:
            if filepath[counter] != "/":
                name = name + filepath[counter]
                counter -= 1
            else:
                break

        return name[::-1] # reverses the string

        return self.get_file_name(filepath) + "_" + column + ".jpg"
