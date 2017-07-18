# histogram.py - This files contains the histogram object used to build a histogram
# Author: Julien Dhouti
# Histogram : class - contains all of the attribute to the histogram object
# Python 3.6.1

import graph
import file_name_generator as fng
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class Histogram(graph.Graph):
    def __init__(self, filepath):
        """Inits Histogram with the filepath of the .csv file we are interested in analyzing.
        
        Args:
            filepath: a string specifying the filepath of the file we wish to analyze.
        """

        super().__init__("histogram", filepath)
        super().set_image(None)
        self.generator = fng.Name_Generator()

    def generate(self, column, ax, bins=None, title=None, color=None):
        """Creates the histogram based on the given information.
            
        Args:
            column: a string specifying the name of the column the data is included in.
            bins: an int representing the amount of bins inside of the histogram.
            title: a string representing the name of the graph.
            color: a string representing the desired color of the graph.
            ax: a subplot where the graph will be drawn on
                
        Returns:
            A tuple containing the figure of the graph along with its subplot. Both are needed to include in 
            a tkinter canvas.
        """

        # Ensures that bins is a positive number. If bins is not given, the plot will determine
        # the amount of bins with respect to the given column.
        if bins == None:
            pass
        elif bins <= 0:
            raise ValueError("The amount of bins should be a positive number.")
        
        # Adjust the color of the graph.
        try:
            super().set_color(color)
        except ValueError:
            print("The given color is unavailable.")

        # Generates the name of the histogram file and assign it to the super class.
        name = self.generator.generate_name(super().get_file_path(), column, "histogram")
        super().set_image_name(name)
        
        # Obtains the values that the user desires to graph.
        values = super().get_data()[column]

        # This is where the histogram function determines the amount of bins if not given any.
        if bins == None:
            ax.hist(values, ec='black', color=super().get_current_color())
        else:
            ax.hist(values, bins=bins, ec='black', color=super().get_current_color())

        ax.set_xlabel(column)
        ax.set_ylabel("Quantity")

        # If a title is given, assign the plot title with the .title() function.
        if title != None:
            ax.set_title(title)

        return ax