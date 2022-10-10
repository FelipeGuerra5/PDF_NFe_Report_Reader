# Imports

import tkinter as tk
from tkinter import filedialog

from _objects.fileclass import reportFile


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


