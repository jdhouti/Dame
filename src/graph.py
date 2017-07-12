# graph.py - This files contains the Graph object
# Author: Julien Dhouti
# Graph : class - contains all of the attribute to the graph object
# Python 3.6.1

import data_object as do

class Graph(do.DataObject):
    def __init__(self, graphType, filepath):
        super().__init__(filepath)
        self.type = graphType
        self.image = None
        self.image_name = None
        self.colors = ['black', 'blue', 'green', 'red', 'yellow', 'orange']
        self.current_color = self.colors[1]

    def get_type(self):
        """Returns the type of the graph (String)."""
        return self.type

    def get_image(self):
        """Returns the Image of the generated graph (Image)"""
        return self.image

    def get_file_path(self):
        """Returns the filepath of the .csv file (String)."""
        return self.filepath

    def get_current_color(self):
        """Returns the current set color for generated graphs (String)."""
        return self.current_color

    def get_colors(self):
        """Returns the available colors for the graph."""
        return self.colors

    def set_image(self, img):
        """Sets the image of the generated graph."""
        self.image = img

    def set_image_name(self, name):
        """Sets the name of the saved image."""
        self.image_name = name

    def change_color(self, color):
        """Changes the color of the graph that can be generated.
        Needs to be done before .generate() function occurs, otherwise
        change will only be applied to the next generated graph.
        """
        if color not in self.colors:
            raise ValueError("Color not found.")
        else:
            self.current_color = self.colors[self.colors.index(color)]
