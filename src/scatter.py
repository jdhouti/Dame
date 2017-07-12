# scatter.py - This files contains the scatter object used to create a scatter object.
# Author: Julien Dhouti
# Scatter : class - contains all of the attribute to the scatter object
# Python 3.6.1
# /Users/Julien/Downloads

import graph
import matplotlib.pyplot as plt
from PIL import Image
import file_name_generator as fng
from sklearn import datasets, linear_model
import os

class Scatter(graph.Graph):
    def __init__(self, filepath):
        super().__init__(self, filepath)
        super().set_image(None)
        self.generator = fng.Name_Generator()

    def generate(self, column1, column2, title=None, color='red'):
        # check to see if the given columns actually exist in the csv file.
        if column1 not in super().get_data().columns:
            raise ValueError(column1 + " cannot be found!")
        if column2 not in super().get_data().columns:
            raise ValueError(column2 + " cannot be found!")
        if column2 == column1:
            raise ValueError("Both columns cannot be the same!")

        super().change_color(color) # set the color of the graph based on the color that was given

        # generate the name for the scatter plot
        name = self.generator.generate_name(super().get_file_path(), column1, "scatter")
        super().set_image_name(name)  # send that name to the graph object

        # using the column name, strip the values from each column using pandas
        col1values = self.data[column1]
        col2values = self.data[column2]

        # ----------------------- create the scatter plot ---------------------- #
        plt.figure()
        plt.plot(col1values, col2values, 'ro', color=color)
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.savefig(name)
        if title != None:
            plt.title(title)
        super().set_image(Image.open(name))  # update the self.image of the graph by giving it a img object
        os.remove(name) # remove the image once we're done with it

    def lin_generate(self, column1, column2, title=None, color='blue'):
        """Generates a linear model. This is just like a regular scatter plot but with a
        linear regression.
        """
        # check to see if the given columns actually exist in the csv file.
        if column1 not in super().get_data().columns:
            raise ValueError(column1 + " cannot be found!")
        if column2 not in super().get_data().columns:
            raise ValueError(column2 + " cannot be found!")
        if column2 == column1:
            raise ValueError("Both columns cannot be the same!")

        # convert given columns into numpy arrays
        column_x = super().get_data()[column1].values
        column_y = super().get_data()[column2].values

        # we want to train 95% of the data and test on 5% so we much split
        # up the given columns accordingly. 
        column_x_train = column_x[:int(column_x.size * 0.95)]
        column_x_test = column_x[-(column_x.size - int(column_x.size * 0.95)):]
        print(column_x_train.size)
        print(column_x_test.size)

        column_y_train = column_y[:int(column_y.size * 0.95)]
        column_y_test = column_y[-(column_y.size - int(column_y.size * 0.95)):]
        print(column_y_test.size)
        print(column_y_train.size)

        column_x_test.reshape(1,-1)
        column_x_train.reshape(1,-1)
        column_y_test.reshape(1,-1)
        column_y_train.reshape(1,-1)

        # create the training model
        regr = linear_model.LinearRegression()
        regr.fit(column_x_train, column_y_train)

        plt.scatter(column_x_test, column_y_test,  color='black')
        plt.plot(column_x_test, regr.predict(column_x_test), color='blue', linewidth=3)

        plt.xticks(())
        lt.yticks(())

        plt.show()

my_scatter = Scatter("/Users/Julien/Downloads/Iris.csv")
my_scatter.lin_generate('SepalLengthCm', 'SepalWidthCm')

