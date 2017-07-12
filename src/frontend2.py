import sys
# matplotlib imports
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi, cos, tan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# Dame imports
import histogram as hist
import data_object as do

# tkinter imports
from tkinter import *
import tkinter as tk
import tkinter.constants
import tkinter.filedialog as tkFileDialog

# note: master = parent

class Application(tk.Frame):
    def __init__(self, master):
        """Initialize the Frame Window for tkinter. Update Gui to show initialize buttons and create the canvas"""


        tk.Frame.__init__(self,master)
        self.master = master
        self.initialize_screen()


    def initialize_screen(self):
        """Places all GUI elements onto the screen - some may be hidden but all are attached to window """


        self.master.title("DAME")
        self.create_visualization_selector()
        self.create_quit_button()
        self.create_canvas()
        self.create_open_file_button()
        self.create_x_column_selector()
        self.create_y_column_selector()
        self.create_column_selector_label()
        self.create_show_visualization_button()

    def initialize_analysis(self):
        """Load all analysis objects needed
            self.analysis_object - DataObject - Used to handle column manipulation on GUI
            self.histogram_object - Histogram - Handles generation of histogram and manipulation"""


        self.analysis_object = do.DataObject(self.filepath)
        self.histogram_object = hist.Histogram(self.filepath)

        # update column selectors with column names from file
        numerical_columns = self.analysis_object.get_num_columns()

        # delete old placeholder column ""
        self.x_column_selector['menu'].delete(0, 'end')
        self.y_column_selector['menu'].delete(0, 'end')

        # add new column options
        for column in numerical_columns:
            self.x_column_selector['menu'].add_command(label=column, command = tk._setit(self.x_column_selected, column))
            self.y_column_selector['menu'].add_command(label=column, command = tk._setit(self.y_column_selected, column))
        

    def create_open_file_button(self):
        """Create button to get filepath for analysis """


        self.open_file_button = Button(self, text='Open File', command = self.open_file)
        self.open_file_button.grid(column=1, row=1, sticky="nesw")

    def open_file(self):
        """stores filepath for the file to be analyzed 
            self.filepath - STRING - contains filepath for analysis file"""


        self.filepath = tkFileDialog.askopenfilename(initialdir = "/",title = "Select data file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print(self.filepath)
        # add code to initialize visualization
        self.initialize_analysis()


    def create_visualization_selector(self):
        """Create OptionMenu to choose from different types of analysis 
            self.var - StringVar - use .get() method to get currently selected visualization type - returns STRING
            self.visualization_selector - OptionMenu - allows user to choose between different visualizations (histogram, scatter plot etc)"""


        OPTIONS = ['Histogram', 'Scatter Plot']
        self.var = StringVar(self.master)
        self.var.set("")
        self.visualization_selector = OptionMenu(self, self.var, *OPTIONS, command = self.determine_visualization_type)
        self.visualization_selector.grid(row = 2, column = 1, sticky = 'nesw')

    def determine_visualization_type(self, event):
        """Determine which visualization to show
            event - STRING - sent by self.visualization_selector when a visualization type is selected"""


        if event == 'Histogram':
            self.set_up_histogram()
        elif event == 'Scatter Plot':
            self.set_up_scatter_plot()

    def set_up_histogram(self):
        """Makes sure x_column_selector is visible and hides y_column_selector """


        if self.x_column_selector_is_visible == False:
            self.x_column_selector.grid()
            self.x_column_selector_is_visible = True
        if self.y_column_selector_is_visible == True:
            self.y_column_selector.grid_remove()
            self.y_column_selector_is_visible = False
        # generate histogram graph here - ACTUALLY MAKE METHOD show_histogram() CALLED BY THE OPTIONMENU TO DO THAT

    

    def show_histogram(self):
        """Generate histogram
            event - STRING - sent by self.x_column_selector when a column is selected"""


        column_name = self.x_column_selected.get()
        # histogram generated here - reference the canvas() method for the variable names to generate the plot
        print("Histogram with " + column_name + " x column to be generated")
        self.f = Figure(figsize = (4,2), dpi = 100)
        self.a = fig.add_subplot(111)
        self.a = self.histogram_object.generate(column_name, self.a)
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, sticky="nesw")
        print("Did it show anything onscreen?")



    def set_up_scatter_plot(self):
        """Makes sure x_column_selector  y_column_selector are visible"""


        if self.x_column_selector_is_visible == False:
            self.x_column_selector.grid() 
            self.x_column_selector_is_visible = True
        if self.y_column_selector_is_visible == False:
            self.y_column_selector.grid() 
            self.y_column_selector_is_visible = True

        # generate scatter plot graph here - ACTUALLY MAKE METHOD show_scatter_plot() CALLED BY THE OPTIONMENU TO DO THAT


    def show_scatter_plot(self):
        """Generate scatter plot
            event - STRING - sent by self.x_column_selector or self.y_column_selector when a column is selected"""


        x_column_name = self.x_column_selected.get()
        y_column_name = self.y_column_selected.get()
        # scatter plot generated here - reference the canvas() method for the variable names to generate the plot
        if x_column_name == "" or y_column_name == "":
            print("Both columns are not filled wont generate scatter plot")
        elif x_column_name == y_column_name:
            print("Both columns are the same cannot plot")
        else:
            print("Scatter plot with " + x_column_name + " x column to be generated and " + y_column_name + " y column to be generated")


    def create_quit_button(self):
        """Create button to quit application"""


        self.quit_button = Button(self, text='Quit', command = self.quit)
        self.quit_button.grid(column=1, row=3, sticky="nesw")


    def create_canvas(self):
        """Creates a canvas object to draw matplotlib visualizations on
            self.f - Figure - contains the figure object for all of the subplots
            self.a - Plot - the plot in question.
            self.canvas - FigureCanvasTkAgg - tkinter widget that holds figure"""


        # leave as placeholder for now
        my_hist = hist.Histogram('../test/Iris.csv')        # you may want to put this somewhere else, this was for testing
        self.a = my_hist.generate('SepalWidthCm', self.a)             # this too
                                                            # so you don't need the objects on lines 153 and 154 and i generate the subplot so get rid of 155 too.

        # self.f = Figure(figsize = (4,2), dpi = 100)
        # self.a = self.f.add_subplot(111)
        # self.a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, sticky="nesw")

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.master) #do we want to keep this? it allows the user to save the plot so probs useful

    def create_x_column_selector(self):
        """Create OptionMenu to choose the column for the x axis
            self.x_column_selected - StringVar - use .get() method to get currently selected x column - returns STRING
            self.x_column_selector - OptionMenu - allows user to choose between different columns
            self.x_column_selector_is_visible - BOOLEAN - if self.x_column_selector is on the screen"""


        # OPTIONS = self.analysis_object.get_num_columns() #replace this with actual columns from the data object
        self.X_OPTIONS = [""]
        self.x_column_selected = StringVar(self.master)
        self.x_column_selected.set("")
        self.x_column_selector = OptionMenu(self, self.x_column_selected, *self.X_OPTIONS)
        self.x_column_selector.grid(row = 2, column = 2, sticky = 'nesw')
        self.x_column_selector.grid_remove()
        self.x_column_selector_is_visible = False

    def create_y_column_selector(self):
        """Create OptionMenu to choose the column for the y axis
            self.y_column_selected - StringVar - use .get() method to get currently selected y column - returns STRING
            self.y_column_selector - OptionMenu - allows user to choose between different columns
            self.y_column_selector_is_visible - BOOLEAN - if self.y_column_selector is on the screen"""


        # OPTIONS = self.analysis_object.get_num_columns() #replace this with actual columns from the data object
        self.Y_OPTIONS = [""]
        self.y_column_selected = StringVar(self.master)
        self.y_column_selected.set("")
        self.y_column_selector = OptionMenu(self, self.y_column_selected, *self.Y_OPTIONS)
        self.y_column_selector.grid(row = 3, column = 2, sticky = 'nesw')
        self.y_column_selector.grid_remove()
        self.y_column_selector_is_visible = False


    def show_visualization(self):
        """Calls whichever visualization method is desired"""


        if self.var.get() == 'Histogram':
            self.show_histogram()
        elif self.var.get() == 'Scatter Plot':
            self.show_scatter_plot()

    def create_column_selector_label(self):
        """Label to indicate this is the area of the screen that holds the column choosers
        self.column_selector_label - Label - Contains some text"""
        

        self.column_selector_label = Label(self, text = 'Choose Column(s)')
        self.column_selector_label.grid(row = 1, column = 2, sticky = 'nesw')

    def create_show_visualization_button(self):
        self.show_visualization_button = Button(self, text='Generate Plot', command = self.show_visualization)
        self.show_visualization_button.grid(row = 4, column = 2)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600+10+10")
    root.resizable(0, 0)
    Application(root).pack(side=tk.TOP)
    root.mainloop()