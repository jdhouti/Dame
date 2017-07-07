# frontend.py - This file holds all of the GUI code
# Author: Tomas Bencomo
# Application : class - sets up and runs GUI commands
# main() : initiate GUI code

# Version 2 - trying to rewrite in python 3

from tkinter import *
import tkinter as tk
import tkinter.constants
import tkinter.filedialog as tkFileDialog
from PIL import Image, ImageTk
import data_analysis as da



class Application(tk.Frame):
    # constructor - builds Tkinter frame
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.master.title('Easy Data Analysis')
        col_count, row_count = self.master.grid_size()

        for col in range(col_count):
            self.master.grid_columnconfigure(col, minsize = 200)

        for row in range(row_count):
            self.master.grid_rowconfigure(row, minsize = 200)

    # prompts user for file that will be analyzed
    # sets 'filepath' attribute to the file path for the analyzed file
    def get_filepath(self):
        # Note - you can only select CSV files right now
        self.filepath = tkFileDialog.askopenfilename(initialdir = "/",title = "Select data file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print(self.filepath)
        # future - once the file is selected, call back end analysis and then draw visualization onscreen
        # Backend calls go here
        self.addAnalysis()


    # places needed buttons onto the screen
    def createWidgets(self):
        self.openButton = tk.Button(self, text = "Open File", command = self.get_filepath)
        self.openButton.grid(row = 0, column = 0)
        # This is just here to easily close the app during testing
        self.quitButton = tk.Button(self, text = "Quit", command = self.quit)
        self.quitButton.grid(row = 1, column = 0)

    # def addAnalysis(self):
    #     """Places visualizations onto the screen after file is chosen"""
    #     self.analyze = da.Data_Analysis(self.filepath)
    #     OPTIONS = ['Histogram', 'Scatter Plot']
    #     self.var = StringVar(self.master)
    #     self.var.set(OPTIONS[0])
    #     analysis_type = OptionMenu(self.master, self.var, *OPTIONS, command = self.update_visualtions)
    #     analysis_type.grid(row = 0, column = 1)

    #     # scatterplot
    #     image = self.analyze.get_scatter_plot('Duration', 'Age')
    #     photo = ImageTk.PhotoImage(image)
    #     scatter_label = Label(image = photo)
    #     scatter_label.image = photo
    #     scatter_label.grid(column = 3, row = 3)

    # def update_visualtions(self, event): #I have no idea why this needs to parameters - LOOK INTO THIS LATER
    #     print(self.var.get())


    # Note - need to clean up the use of global variables for var - check if just use the event argument passed to update_visualizations() instead
    def addAnalysis(self):
        """Controls how visualization is handled onscreen. Used to create Data_Analysis object. visualization_type is an OptionMenu that chooses
        which visualization the user wants to see (histogram, scatter plot, etc). update_visualizations() deals with the actual drawing of widgets"""
        #  create analysis object
        self.analyze = da.Data_Analysis(self.filepath)
        #  create and populate OptionMenu to choose which visualization
        OPTIONS = ['Histogram', 'Scatter Plot']
        self.var = StringVar(self.master)
        self.var.set("")
        visualization_type = OptionMenu(self.master, self.var, *OPTIONS, command = self.update_visualtions)
        visualization_type.grid(row = 0, column = 3)

    def update_visualtions(self, event):
        """Determines the type of visualtion user wants and calls respective method to display that visualization """

        if event == 'Histogram':
            self.show_histogram(self.analyze)
        elif event == 'Scatter Plot':
            self.show_scatter_plot(self.analyze)

    def show_histogram(self, data_analysis_object):
        print("Histogram will be shown")

    def show_scatter_plot(self, data_analysis_object):
        """Create OptionMenus for x and y axis and set up display_scatter() to be called if both OptionMenus have columns selected"""
        """todo: check to make sure the columns are both numerical in type, fix spacing of the x and y axis OptionMenus.
        Try filtering columns only by numerical value? """
        print("Scatter plot will be shown")

        # self.x_axis_label = Label(self, text = "X Axis")
        # self.x_axis_label.grid(row = 1, column = 2)
        # self.y_axis_label = Label(self, text = "Y Axis")
        # self.y_axis_label.grid(row = 1, column = 3)
        column_names = data_analysis_object.get_columns()
        self.x_column_name = StringVar(self.master)
        self.x_column_name.set("")
        self.x_axis_selector = OptionMenu(self.master, self.x_column_name, *column_names, command = self.display_scatter)
        self.x_axis_selector.grid(row = 2, column = 2)
        self.y_column_name = StringVar(self.master)
        self.y_column_name.set("")
        self.y_axis_selector = OptionMenu(self.master, self.y_column_name, *column_names, command = self.display_scatter)
        self.y_axis_selector.grid(row = 2, column = 3)

    def display_scatter(self, event):
        """Check that both x and y axis have been selected from the columns. Then draws scatterplot onscreen"""
        print("The event parameter = " + event)
        if self.x_column_name.get() != "" and self.y_column_name.get() != "":
            # we can display something
            self.image = self.analyze.get_scatter_plot(self.x_column_name.get(), self.y_column_name.get())
            self.plot_photo = ImageTk.PhotoImage(self.image)
            self.plot_label = Label(image = self.plot_photo)
            self.plot_label.image = self.plot_photo
            self.plot_label.grid(row = 3, column = 2)



def main():
    root = Tk()
    app = Application(root)
    # app.master.title('Easy Data Analysis')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w * .7, h * .7))
    root.mainloop()


if __name__ == "__main__": main()
