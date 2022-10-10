from  _objects.fileclass import reportFile
from _functions.functions import *

def main():

    dic ={}

    # Assign each pdf for a reportFile Class
    files = openFiles()
    for i, file in enumerate(files):
        dic[f'file_name{i}'] = reportFile(file)


    # Login in the terminal
    for key in dic:

        # Files caracteristics for Debug
        print('\n[START OF FILE]' + '-'* 30 + '[START OF FILE]\n')
        print(f'[FILE NAME] {dic[key].file_name} ')
        print(f'[FILE TYPE] {dic[key].file_type} ')
        print(f'[FILE DATA] {dic[key].file_data} ')
        print('\n[END OF FILE]' + '-'* 30 + '[END OF FILE]\n')


    print(f'[DICTONARY OF CLASSES] {dic}')

if __name__ == "__main__":
    main()
