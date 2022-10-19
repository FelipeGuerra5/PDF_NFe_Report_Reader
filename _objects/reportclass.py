import pandas as pd
import numpy as np
import fitz
import tkinter

# Functions for Each Type of NFe
from _objects.comercio_cacau import getDataOMCom
from _objects.santa_fe import getDataSantaFe


class reportFile:
    def __init__(self, file):
        self.file_path = file
        self.file_name = self.setName(file)
        self.file_text = self.setText(file)
        self.file_type = self.setType(self.file_text)
        
        # Obs: The file_data must return an array with 5 itemns
        self.file_data = fileSorter(self.file_type, self)
        print(self.file_data)

    def setText(self, file):
        text = ""
        with fitz.open(file) as doc:
            for page in doc:
                text += page.get_text()
        return text.lower()

    def setType(obj, text):
        file_type = ''
        if text.find('om comercio de cacau ltda') != -1:
            file_type = 'comercio_de_cacau_ltda'
        elif text.find('comercial santa fé') != -1:
            file_type = 'comercial_de_santa_fe'
        else:    
            file_type = 'Not Found'
        return file_type

    def setName(self, file):
        full_name = str(file)
        start = full_name.rfind('/')
        file_name = full_name[start + 1 : ]
        return file_name

# Sort the files based on the "fileClass.file_type"
# For inserting a new type you have to set a new file_type on function setType(), above.
def fileSorter(file_type, obj):
    if file_type == 'comercio_de_cacau_ltda':
        file_data = getDataOMCom(obj)
        print(f'[FILE DATA] {file_data}')
        return file_data
    
    elif file_type == 'comercial_de_santa_fe':
        file_data = getDataSantaFe(obj)
        print(f'[FILE DATA] {file_data}')
        return file_data

    else:
        return 'Not_suported_File'
