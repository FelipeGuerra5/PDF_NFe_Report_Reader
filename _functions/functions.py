# Imports
from codecs import latin_1_decode
import pandas as pd
import numpy as np
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
    try:
        df = pd.read_csv(
            'Main_do_not_use.csv', 
            encoding='latin1', 
            dtype={
                'nfe_number' : str, 
                'quantity_(KG)' : int
                }
        )
        
        # append dic fiel.file_data to the table.
        for row in file.file_data:
            row['file_name'] = file.file_name
            print(F'[ROW OF FILE.FILE_DATA] {row}')
            new_row = pd.DataFrame([row])

            df = pd.concat([new_row, df], ignore_index=True)

        # Save
        df.to_csv('Main_do_not_use.csv', encoding='latin1')
        df.to_excel("Invoice Report.xlsx")

    except: 
        df = pd.DataFrame(columns=[
            'date_of_transaction', 
            'farmer_cpf',
            'farmer', 
            'quantity_(KG)',
            'nfe_number',
            'key',
            'file_name'
        ])

    # append dic fiel.file_data to the table.
        for row in file.file_data:
            row['file_name'] = file.file_name
            print(F'[ROW OF FILE.FILE_DATA] {row}')
            new_row = pd.DataFrame([row])

            df = pd.concat([new_row, df], ignore_index=True)
        
        # Save
        df.to_csv('Main_do_not_use.csv', encoding='latin1')
        df.to_excel("Invoice Report.xlsx")
