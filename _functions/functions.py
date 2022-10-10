# Imports

import tkinter as tk
from tkinter import filedialog

from _objects.reportclass import reportFile


#  Functions

def openFiles():
    # Instance of Win explorer
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()

    return files

def getName(file):
        full_name = str(file)
        start = full_name.rfind('/')
        file_name = full_name[start : ]
        
        return file_name

def toTable(file):
    # try to open a csv file.
    # if there is one so open it
    # if not create one
    # append dic fiel.file_data to the table.
    pass