import re

def getDataGandu(obj):

    # Find cliente
    client_indx = obj.file_text.find('cliente:')
    end_indx = obj.file_text[client_indx: ].find('\n')
    name = obj.file_text[client_indx + 16 : client_indx + end_indx]

    # Parameters for the RegEx
    nm = name + '\n'
    dt = '\d\d/\d\d/\d\d\d\d\n'
    i =  '.*\n'
    f = '.*\n'
    superstring = nm + dt + i + f + dt + i + f + f 

    all_data = []
    blocks = getLines(obj.file_text, superstring)

    for block in blocks:    
        data = {}
        data['date_of_transaction'] = getTransactionDate(block)
        data['farmer_cpf'] = getCpf(block)
        data['farmer'] = name.title()
        data['quantity_(KG)'] = getQuantity(block)
        data['nfe_number'] = getNfeNumber(block)
        data['key'] = getKey(block)
        all_data.append(data)
    
    return all_data

# Methods for extracting the data from text
def getLines(text, superstring):
    r = re.compile(superstring)
    blocks = r.findall(text)
    return blocks

def getKey(text):
    return ''

def getTransactionDate(block):
    r = re.compile('\d\d/\d\d/\d\d\d\d')
    dates = r.findall(block)
    date = dates[0]
    return date

def getCpf(text):
    return ''

def getQuantity(block):
    end_idx = block.rfind('\n')
    end_idx = block[ : end_idx - 1].rfind('\n')
    start_idx = block[ : end_idx - 1].rfind('\n')
    qtt = block[start_idx + 1 : end_idx]
    qtt = qtt
    coma_idx = qtt.find(',')
    qtt = int(qtt[ : coma_idx])
    return qtt

def getNfeNumber(block):
    r = re.compile('\d\d\d\d\d\d')
    nfe_n_arr = r.findall(block)
    nfe_n = str(nfe_n_arr[0])
    return nfe_n
