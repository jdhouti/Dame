# graph.py - This files contains the Graph object
# Author: Julien Dhouti
# Graph : class - contains all of the attribute to the graph object
# Python 3.6.1

import pandas as pd

class Graph:
    def __init__(self, graphType, filepath):
        self.type = graphType
        self.image = None
        self.imageName = None
        self.filepath = filepath
        self.data = pd.read_csv(filepath)   # data contains the file path of the object
        self.colors = ['black', 'blue', 'green', 'red', 'yellow', 'orange']
        self.currentColor = self.colors[1]

    def getType(self):
        """Returns the type of the graph (String)."""
        return self.type

    def getData(self):
        """Returns the panda series of the given data for each graph. (panda.Series)"""
        return self.data

    def getImage(self):
        """Returns the Image of the generated graph (Image)"""
        return self.image

    def getFilePath(self):
        """Returns the filepath of the .csv file (String)."""
        return self.filepath

    def getCurrentColor(self):
        """Returns the current set color for generated graphs (String)."""
        return self.currentColor

    def getColors(self):
        """Returns the available colors for the graph."""
        return self.colors

    def setImage(self, img):
        """Sets the image of the generated graph."""
        self.image = img

    def setImageName(self, name):
        """Sets the name of the saved image."""
        self.imageName = name

    def changeColor(self, color):
        """Changes the color of the graph that can be generated.
        Needs to be done before .generate() function occurs, otherwise
        change will only be applied to the next generated graph.
        """
        if color not in self.colors:
            raise ValueError("Color not found.")
        else:
            self.currentColor = self.colors[self.colors.index(color)]
