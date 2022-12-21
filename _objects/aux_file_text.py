# from _functions.functions import openFiles, getName

import tkinter as tk
from tkinter import filedialog
import fitz

def showText(files):
    for file in files:
        print(f'[FILENAME] --> {getName(file)} ')
        text = getText(file)
        print(f'[FILETEXT] --> {text} ')


def getText(file):
    text = ""
    with fitz.open(file) as doc:
        for page in doc:
            text += page.get_text()
        print(f'[TEXT] {text}')
    return text.lower()

if __name__ == "__main__":
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

    files = openFiles()
    showText(files)