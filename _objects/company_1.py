import re

def getDataOMCom(obj):
   
    all_data = []
    lines = getLines(obj.file_text)
    
    for line in lines:    
        data = {}
        data['date_of_transaction'] = getTransactionDate(line)
        data['farmer_cpf'] = getCpf(line)
        data['farmer'] = getFarmer(line, data['farmer_cpf'])
        data['quantity_(KG)'] = getQuantity(line)
        data['nfe_number'] = getNfeNumber(line)
        data['key'] = getKey(line)
        all_data.append(data)

    return all_data    

# Parameters for the RegEx
dt = '\d\d/\d\d/\d\d\d\d\n'
nm = '.*\n'
nm_exc = '.*'
cpf = '\d\d\d.\d\d\d.\d\d\d-\d\d\n'
num = ' \d\d.\d\d\d\n'
val = ' .*.\d\d\n'
key = '\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d'

superstring = dt + nm + cpf + num + val + key
superstring_exc = dt + nm_exc + cpf + num + val + key

# Methods for extracting the data from text
def getLines(text):
    r = re.compile(superstring)
    lines_array = r.findall(text)
    try:
        r = re.compile(superstring_exc)
        excp_array = r.findall(text)
        if len(excp_array) > 0:
            for item in excp_array:
                lines_array.append(item)
    except:
        print('no exception')
    return lines_array

def getKey(text):
    return text[-44 : ]

def getFarmer(text, cpf):
    text = text[10 : ].title()
    idx_start = text.find('\n')
    idx_end = text[idx_start + 1 : ].find(cpf)
    text = text[idx_start + 1 : idx_end + 1]
    return text

def getTransactionDate(text):
    return text[ : 10]

def getCpf(text):
    cpf = '\d\d\d.\d\d\d.\d\d\d-\d\d'
    r = re.compile(cpf)
    cpf = r.findall(text)
    text = cpf[0]
    print(cpf[0])
    return text

def getQuantity(text):
    text = text[-55 : -44]
    idx_start = text.find('\n')
    idx_end = text[idx_start + 1 : ].find(',')
    text = text[idx_start + 1 : idx_start + idx_end + 1]
    text = text.replace('.', '')
    text = int(text)
    return text

def getNfeNumber(text):
    primary = text[-62 : -50]
    idx = primary.find('.')
    string = str(primary[idx -2 : idx + 4])
    return string