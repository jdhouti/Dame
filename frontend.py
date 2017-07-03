# frontend.py - This file holds all of the GUI code
# Author: Tomas Bencomo

from Tkinter import *
import Tkinter as tk 
import Tkconstants
import tkFileDialog



class Application(tk.Frame):
    # constructor - builds Tkinter frame
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    # prompts user for file that will be analyzed
    # sets 'filepath' attribute to the file path for the analyzed file
    def get_filepath(self):
        # Note - you can only select CSV files right now
        self.filepath = tkFileDialog.askopenfilename(initialdir = "/",title = "Select data file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print self.filepath
        # future - once the file is selected, call back end analysis and then draw visualization onscreen
    # places needed buttons onto the screen
    def createWidgets(self):
        self.openButton = tk.Button(self, text = "Open File", command = self.get_filepath)
        self.openButton.grid()
        # This is just here to easily close the app during testing
        self.quitButton = tk.Button(self, text = "Quit", command = self.quit)
        self.quitButton.grid(column = 5, row = 5)

app = Application()
app.master.title('Easy Data Analysis')
app.mainloop()