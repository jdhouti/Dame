import sys
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi, cos, tan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
# from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

from tkinter import *
import tkinter as tk
import tkinter.constants
import tkinter.filedialog as tkFileDialog
from PIL import Image, ImageTk

# master = parent

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.initialize_screen()


    def initialize_screen(self):
        self.master.title("DAME")
        self.visualization_selector()
        self.quit_button()
        self.canvas()
        self.open_file_button()
        self.x_column_selector()
        self.y_column_selector()
        self.column_selector_label()


    def open_file_button(self):
        self.open_file_button = Button(self, text='Open File', command = self.open_file)
        self.open_file_button.grid(column=1, row=1, sticky="nesw")

    def open_file(self):
        self.filepath = tkFileDialog.askopenfilename(initialdir = "/",title = "Select data file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print(self.filepath)
        # add code to initialize visualization


    def visualization_selector(self):
        OPTIONS = ['Histogram', 'Scatter Plot']
        self.var = StringVar(self.master)
        self.var.set("")
        self.visualization_selector = OptionMenu(self, self.var, *OPTIONS, command = self.determine_visualization_type)
        self.visualization_selector.grid(row = 2, column = 1, sticky = 'nesw')

    def determine_visualization_type(self, event):
        # todo
        if event == 'Histogram':
            self.set_up_histogram()
        elif event == 'Scatter Plot':
            self.set_up_scatter_plot()

    def set_up_histogram(self):
        
        if self.x_column_selector_is_visible == False:
            self.x_column_selector.grid()
            self.x_column_selector_is_visible = True
        if self.y_column_selector_is_visible == True:
            self.y_column_selector.grid_remove()
            self.y_column_selector_is_visible = False
        # generate histogram graph here - ACTUALLY MAKE METHOD show_histogram() CALLED BY THE OPTIONMENU TO DO THAT

    

    def set_up_scatter_plot(self):

        if self.x_column_selector_is_visible == False:
            self.x_column_selector.grid() 
            self.x_column_selector_is_visible = True
        if self.y_column_selector_is_visible == False:
            self.y_column_selector.grid() 
            self.y_column_selector_is_visible = True

        # generate scatter plot graph here - ACTUALLY MAKE METHOD show_scatter_plot() CALLED BY THE OPTIONMENU TO DO THAT


       


    def quit_button(self):
        self.quit_button = Button(self, text='Quit', command = self.quit)
        self.quit_button.grid(column=1, row=3, sticky="nesw")


    def canvas(self):
        self.f = Figure(figsize = (4,2), dpi = 100)
        self.a = self.f.add_subplot(111)
        self.a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=1, rowspan=5, sticky="nesw")

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.master)

    def x_column_selector(self):
        OPTIONS = ['Column1', 'Column2']
        self.x_column_selected = StringVar(self.master)
        self.x_column_selected.set("")
        self.x_column_selector = OptionMenu(self, self.x_column_selected, *OPTIONS)
        self.x_column_selector.grid(row = 2, column = 2, sticky = 'nesw')
        self.x_column_selector.grid_remove()
        self.x_column_selector_is_visible = False

    def y_column_selector(self):
        OPTIONS = ['Column1', 'Column2']
        self.y_column_selected = StringVar(self.master)
        self.y_column_selected.set("")
        self.y_column_selector = OptionMenu(self, self.y_column_selected, *OPTIONS)
        self.y_column_selector.grid(row = 3, column = 2, sticky = 'nesw')
        self.y_column_selector.grid_remove()
        self.y_column_selector_is_visible = False

    def column_selector_label(self):
        self.column_selector_label = Label(self, text = 'Choose Column(s)')
        self.column_selector_label.grid(row = 1, column = 2, sticky = 'nesw')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600+10+10")
    root.resizable(0, 0)
    Application(root).pack(side=tk.TOP)
    root.mainloop()