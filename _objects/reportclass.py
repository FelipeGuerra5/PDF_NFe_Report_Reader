import pandas as pd
import numpy as np
import fitz
import tkinter

# Functions for Each Type of NFe
from _objects.company_1 import getDataOMCom
from _objects.company_2 import getDataSantaFe
from _objects.company_3 import getDataGandu

class reportFile:
    def __init__(self, file):
        self.file_path = file
        self.file_name = self.setName(file)
        self.file_text = self.setText(file)
        self.file_type = self.setType(self.file_text)
        
        # Obs: The file_data must return an array with 5 itemns
        self.file_data = fileSorter(self.file_type, self)

    def setText(self, file):
        text = ""
        with fitz.open(file) as doc:
            for page in doc:
                text += page.get_text()
            # print(f'[TEXT] {text}')
        return text.lower()


    def setType(obj, text):
        file_type = ''
        # First Company
        if text.find('om comercio de cacau ltda') != -1:
            file_type = 'comercio_de_cacau_ltda'
        # Second Company
        elif text.find('comercial santa fé') != -1:
            file_type = 'comercial_de_santa_fe'
        # Third company
        elif text.find('cooperativa agricola gandu ltda') != -1:
            file_type = 'cooperativa_agricola_gandu'
        # Company not found
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
    # First Company
    if file_type == 'comercio_de_cacau_ltda':
        file_data = getDataOMCom(obj)
        return file_data
    
    # Second Company
    elif file_type == 'comercial_de_santa_fe':
        file_data = getDataSantaFe(obj)
        return file_data
    
    # Third company
    elif file_type == 'cooperativa_agricola_gandu':
        file_data = getDataGandu(obj)
        for file in file_data:
            print(f'[FILE DATA] -> {file} ')
        return file_data
    
    # Company not found
    else:
        return 'Not_suported_File'

if __name__=="__main__":
    pass