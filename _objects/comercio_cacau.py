import re

def getDataOMCom(obj):
    # For testing
    print('[GETING DATA FROM COMERCIO CACAU]')
    
    all_data = []

    lines = getLines(obj.file_text)
    
    for line in lines:
    
        data = {}
        data['key'] = getKey(line)
        data['farmer'] = getFarmer(line)
        data['date_of_transaction'] = getTransactionDate(line)
        data['quantity'] = getQuantity(line)
        data['farmer_cpf'] = getCpf(line)
        data['nfe_number'] = getNfeNumber(line)
        
        all_data.append(data)
    
    print('[ALL DATA]')
    for item in all_data:
        print(item)

    return all_data    
# Parameters for the RegEx
dt = '\d\d/\d\d/\d\d\d\d\n'
nm = '.*\n'
cpf = '\d\d\d.\d\d\d.\d\d\d-\d\d\n'
num = ' \d\d.\d\d\d\n'
val = ' .*.\d\d\n'
key = '\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d'
superstring = dt + nm + cpf + num + val + key


# Methods for extracting the data from text
def getLines(text):
    r = re.compile(superstring)
    lines_array = r.findall(text)
    return lines_array

def getKey(text):
    return text[-44 : ]

def getFarmer(text):
    text = text[10 : -70].title()
    idx_start = text.find('\n')
    idx_end = text[idx_start + 1 : ].find('\n')
    text = text[idx_start + 1 : idx_end + 1]
    return text

def getTransactionDate(text):
    return text[ : 10]

def getQuantity(text):
    pass

def getCpf(text):
    return text[-75 : -61]

def getNfeNumber(text):
    primary = text[-62 : -51]
    idx = primary.find('.')
    return primary[idx -2 : idx + 4]