import time

from  _objects.reportclass import reportFile
from _functions.functions import *

def main():

    dic ={}

    # Assign each pdf for a reportFile Class
    files = openFiles()
    for i, file in enumerate(files):
        try:
            dic[f'file_name{i}'] = reportFile(file)
        except:
            file_name = getName(file)
            file_name = file_name[1 : ]
            alertUser(file_name)

    # Login in the terminal
    for invoice in dic:

        # Files caracteristics for Debug
        print('\n[START OF FILE]' + '-'* 30 + '[START OF FILE]\n')
        print(f'[FILE NAME] {dic[invoice].file_name} ')
        print(f'[FILE TYPE] {dic[invoice].file_type} ')
        print(f'[LINE DATA] {dic[invoice].file_data} ')
        print('\n[END OF FILE]' + '-'* 45 + '[END OF FILE]\n')
        toTable(dic[invoice])
    
    print('\n[TABLE DONE]' + '-'* 45 + '[TABLE DONE]\n')
    time.sleep(1)
 
if __name__ == "__main__":
    main()
