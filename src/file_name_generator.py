# generator.py - This file contains the functions that generate the names for the
# files generated in the data_analysis.py file.
# Author: Julien Dhouti

import random

class Name_Generator:
    def __init__(self):
        self.generatedNames = []

    def get_generatedNames(self):
        return self.generatedNames

    def generate_name(self):
        while True:
            name = str(random.randint(1, 100000)) + ".png"

            if name in self.generatedNames:
                continue
            else:
                self.generatedNames.append(name)
                break

        return name
