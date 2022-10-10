# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# NEXT WORK DAY
    # In order oto find what I want first: find all cpf,
    #  for they do not repeat.
        # then:
    # find index of each CPF
    # find the index for the -> Totais do fornecedor:
    # get all info from one '\n' back from cpf and 2 '\n' after Totais do fornecedor:
        # then
    # extract each block of invoice using the same name and cpf
    # return this as info for the sortData function

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import re

def getDataSantaFe(obj):
    
    all_data = []

    lines = getLines(obj.file_text)

    for line in lines:    
        data = {}
        data['date_of_transaction'] = getTransactionDate(line)
        data['farmer_cpf'] = getCpf(line)
        data['farmer'] = getFarmer(line)
        data['quantity_(KG)'] = getQuantity(line)
        data['nfe_number'] = getNfeNumber(line)
        data['key'] = getKey(line)
        all_data.append(data)

    return all_data    

# ANTONIO TIAGO DOS SANTOS
# 349.893.665-49 -> good for anchor

nm = '.*\n'
cpf = '\d\d\d.\d\d\d.\d\d\d-\d\d\n'
tt = '\totais do fornecedor:'
qtt = '.*\n'
avg = '.*\n'

superstring = nm + cpf + we + tt + qtt + avg


def getLines(text):
    print('[GET LINES]')
    r = re.compile(nm + cpf)
    lines_array = r.findall(text)
    for line in lines_array:
        print(f'[EACH LINE FOR LINES_ARRAY] {line} {l}')
    return lines_array

def getKey(text):
    return text[-44 : ]

def getFarmer(text):
   pass

def getTransactionDate(text):
    pass


def getCpf(text):
    pass


def getQuantity(text):
    pass


def getNfeNumber(text):
    pass
