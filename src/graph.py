# graph.py - This files contains the Graph object
# Author: Julien Dhouti
# Graph : class - contains all of the attribute to the graph object
# Python 3.6.1

import pandas as pd

class Graph:
    def __init__(self, graphType, title, data):
        self.type = graphType
        self.title = title
        self.image = None
        self.data = pd.read_csv(data)   # data contains the file path of the object
        self.colors = ['black', 'blue', 'green', 'red', 'yellow', 'orange']
        self.currentColor = self.colors[3]

    def getType(self):
        return self.type

    def getTitle(self):
        return self.title

    def getData(self):
        return self.data

    def setImage(self, img):
        self.image = img

    def changeColor(self, color):
        if color not in self.colors:
            raise ValueError("Cannot recognize color.")
        else:
            self.currentColor = self.currentColor[self.currentColor.index(color)]
