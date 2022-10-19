from  _objects.reportclass import reportFile
from _functions.functions import *

def main():

    dic ={}

    # Assign each pdf for a reportFile Class
    files = openFiles()
    for i, file in enumerate(files):
        dic[f'file_name{i}'] = reportFile(file)


    # Login in the terminal
    for invoice in dic:

        # Files caracteristics for Debug
        print('\n[START OF FILE]' + '-'* 30 + '[START OF FILE]\n')
        print(f'[FILE NAME] {dic[invoice].file_name} ')
        print(f'[FILE TYPE] {dic[invoice].file_type} ')
        for data in dic[invoice].file_data:
            print(f'[FILE DATA] {data} ')
        print('\n[END OF FILE]' + '-'* 30 + '[END OF FILE]\n')

        toTable(dic[invoice])        

    print(f'[DICTONARY OF CLASSES] {dic}')

if __name__ == "__main__":
    main()
