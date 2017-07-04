# frontend.py - This file holds all of the GUI code
# Author: Tomas Bencomo
# Application : class - sets up and runs GUI commands
# main() : initiate GUI code

# Version 2 - trying to rewrite in python 3

from tkinter import *
import tkinter as tk
import tkinter.constants
import tkinter.filedialog



class Application(tk.Frame):
    # constructor - builds Tkinter frame
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.master.title('Easy Data Analysis')
    # prompts user for file that will be analyzed
    # sets 'filepath' attribute to the file path for the analyzed file
    def get_filepath(self):
        # Note - you can only select CSV files right now
        self.filepath = tkFileDialog.askopenfilename(initialdir = "/",title = "Select data file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print(self.filepath)
        # future - once the file is selected, call back end analysis and then draw visualization onscreen
        # Backend calls go here


    # places needed buttons onto the screen
    def createWidgets(self):
        self.openButton = tk.Button(self, text = "Open File", command = self.get_filepath)
        self.openButton.grid(row = 0, column = 0)
        # This is just here to easily close the app during testing
        self.quitButton = tk.Button(self, text = "Quit", command = self.quit)
        self.quitButton.grid(column = 0, row = 1)
        self.tempLabel = tk.Label(self, text = 'Placeholder for visualizations', font=("Helvetica", 40))
        self.tempLabel.grid(column = 1, row = 0)






def main():
    root = Tk()
    app = Application(root)
    # app.master.title('Easy Data Analysis')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w * .7, h * .7))
    root.mainloop()


if __name__ == "__main__": main()
