import sys
# matplotlib imports
from numpy import arange, sin, pi, cos, tan
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# Dame imports
import histogram as hist
import data_object as do
import scatter as sc

# tkinter imports - old imports only worked for python 3
# from tkinter import *
# import tkinter as tk
# import tkinter.constants
# import tkinter.filedialog as tkFileDialog


# handle different python versions
from sys import version_info
if version_info.major == 2:
    # We are using Python 2.x
    from Tkinter import *
    import Tkinter as tk
    import Tkinter, Tkconstants, tkFileDialog
elif version_info.major == 3:
    # We are using Python 3.x
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
        self.create_linear_regression_button()
        self.create_same_columns_warning_label()

    def initialize_analysis(self):
        """Load all analysis objects needed
            self.analysis_object - DataObject - Used to handle column manipulation on GUI
            self.histogram_object - Histogram - Handles generation of histogram and manipulation"""


        self.analysis_object = do.DataObject(self.filepath)
        self.histogram_object = hist.Histogram(self.filepath)
        self.scatter_object = sc.Scatter(self.filepath)
        self.master.title("DAME - " + self.analysis_object.get_name()) #IMO this looks nicer

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
        self.var.set("Analysis")
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
        """Makes sure x_column_selector is visible and hides y_column_selector and linear_regression_button is hidden """


        if self.x_column_selector_is_visible == False:
            self.x_column_selector.grid()
            self.x_column_selector_is_visible = True
        
        if self.y_column_selector_is_visible == True:
            self.y_column_selector.grid_remove()
            self.y_column_selector_is_visible = False
        
        if self.linear_regression_button_isVisible == True:
            self.linear_regression_button.grid_remove()
            self.linear_regression_button_isVisible = False
        
        if self.same_columns_warning_label_isVisible == True:
            self.same_columns_warning_label.grid_remove()
            self.same_columns_warning_label_isVisible = False

    

    def show_histogram(self):
        """Generate histogram
            event - STRING - sent by self.x_column_selector when a column is selected"""


        column_name = self.x_column_selected.get()
        # histogram generated here - reference the canvas() method for the variable names to generate the plot
        print("Histogram with " + column_name + " x column to be generated")
        self.f = Figure(figsize = (6,4), dpi = 100)
        self.a = self.f.add_subplot(111)
        self.a = self.histogram_object.generate(column_name, self.a)
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, sticky="nesw")



    def set_up_scatter_plot(self):
        """Makes sure x_column_selector, linear_regression_button, and y_column_selector are visible"""


        if self.x_column_selector_is_visible == False:
            self.x_column_selector.grid() 
            self.x_column_selector_is_visible = True
        
        if self.y_column_selector_is_visible == False:
            self.y_column_selector.grid() 
            self.y_column_selector_is_visible = True
        
        if self.linear_regression_button_isVisible == False:
            self.linear_regression_button.grid()
            self.linear_regression_button_isVisible = True
        
        if self.same_columns_warning_label_isVisible == True:
            self.same_columns_warning_label.grid_remove()
            self.same_columns_warning_label_isVisible = False



    def show_scatter_plot(self):
        """Generate scatter plot
            event - STRING - sent by self.x_column_selector or self.y_column_selector when a column is selected"""


        x_column_name = self.x_column_selected.get()
        y_column_name = self.y_column_selected.get()
        # scatter plot generated here - reference the canvas() method for the variable names to generate the plot
        if x_column_name == "" or y_column_name == "":
            print("Both columns are not filled wont generate scatter plot")
        elif x_column_name == y_column_name:
            # print("Both columns are the same cannot plot")
            self.same_columns_warning_label.grid()
            self.same_columns_warning_label_isVisible = True
        else:
             # make sure warning label isnt there
            if self.same_columns_warning_label_isVisible == True:
                self.same_columns_warning_label.grid_remove()
                self.same_columns_warning_label_isVisible = False


            self.f = Figure(figsize = (6,4), dpi = 100)
            self.a = self.f.add_subplot(111)
            self.a = self.scatter_object.generate(x_column_name, y_column_name, self.a)
            self.canvas = FigureCanvasTkAgg(self.f, master=self)
            self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, sticky="nesw")


    def show_regression_scatter_plot(self):
        """Generate scatter plot with a regression line
            event - STRING - sent by self.x_column_selector or self.y_column_selector when a column is selected"""


        x_column_name = self.x_column_selected.get()
        y_column_name = self.y_column_selected.get()
        # scatter plot generated here - reference the canvas() method for the variable names to generate the plot
        if x_column_name == "" or y_column_name == "":
            print("Both columns are not filled wont generate scatter plot")
        elif x_column_name == y_column_name:
            # print("Both columns are the same cannot plot")
            self.same_columns_warning_label.grid()
            self.same_columns_warning_label_isVisible = True
        else:

            # make sure warning label isnt there
            if self.same_columns_warning_label_isVisible == True:
                self.same_columns_warning_label.grid_remove()
                self.same_columns_warning_label_isVisible = False


            self.f = Figure(figsize = (6,4), dpi = 100)
            self.a = self.f.add_subplot(111)
            self.a = self.scatter_object.lin_generate(x_column_name, y_column_name, self.a)
            self.canvas = FigureCanvasTkAgg(self.f, master=self)
            self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, sticky="nesw")


    def create_quit_button(self):
        """Create button to quit application"""


        self.quit_button = Button(self, text='Quit', command = self.quit)
        self.quit_button.grid(column=1, row=3, sticky="nesw")


    def create_canvas(self):
        """Creates a canvas object to draw matplotlib visualizations on
            self.f - Figure - contains the figure object for all of the subplots
            self.a - Plot - the plot in question.
            self.canvas - FigureCanvasTkAgg - tkinter widget that holds figure"""


        self.f = Figure(figsize = (6,4), dpi = 100)
        self.a = self.f.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, columnspan = 6, sticky="nesw")

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.master) #do we want to keep this? it allows the user to save the plot so probs useful

    def create_x_column_selector(self):
        """Create OptionMenu to choose the column for the x axis
            self.x_column_selected - StringVar - use .get() method to get currently selected x column - returns STRING
            self.x_column_selector - OptionMenu - allows user to choose between different columns
            self.x_column_selector_is_visible - BOOLEAN - if self.x_column_selector is on the screen"""


        # OPTIONS = self.analysis_object.get_num_columns() #replace this with actual columns from the data object
        self.X_OPTIONS = [""]
        self.x_column_selected = StringVar(self.master)
        self.x_column_selected.set("x column")
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
        self.y_column_selected.set("y column")
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

    def create_linear_regression_button(self):
        """Create button used to generate scatter plots with linear regression line applied
        self.linear_regression_button - Button - click to show plot with regression line
        self.linear_regression_button_isVisible - BOOLEAN - True if button visible on screen"""


        self.linear_regression_button = Button(self, text = 'Apply Linear Reg', command = self.show_regression_scatter_plot)
        self.linear_regression_button.grid(row = 5, column = 2)
        self.linear_regression_button.grid_remove()
        self.linear_regression_button_isVisible = False


    def create_same_columns_warning_label(self):
        """Create Label that alerts user if they have selected the same column for 2 different axis
        self.same_columns_warning_label - Label - alert user if same column selected twice
        self.same_columns_warning_label_isVisible - BOOLEAN - True if same_columns_warning_label visible on screen"""


        self.same_columns_warning_label = Label(self, text='Same Column Selected Twice', fg = 'red')
        self.same_columns_warning_label.grid(row = 6, column = 2)
        self.same_columns_warning_label.grid_remove()
        self.same_columns_warning_label_isVisible = False

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("875x475+10+10")
    root.resizable(0, 0)
    Application(root).pack(side=tk.TOP)
    # root.mainloop()
    while True:
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass