import re

def getDataSantaFe(obj):
    
    all_data = []
    user_block = getUserBlock(obj.file_text)
    
    for block in user_block:    
        for inv in user_block[block]['invoices']:
            data = {}
            data['date_of_transaction'] = getTransactionDate(inv)
            data['farmer_cpf'] = block
            data['farmer'] = user_block[block]['name'].title()
            data['nfe_number'] = getNfeNumber(inv)
            data['quantity_(KG)'] = getQuantity(inv, data['nfe_number'])
            data['key'] = getKey(inv)
            all_data.append(data)
    
    return all_data
    
def getUserBlock(text):
    # Find all cpfs
    r = re.compile('\d\d\d.\d\d\d.\d\d\d-\d\d')
    users = r.findall(text)

    user_block = {}

    # Find all Access keys inside it
    for i, user in enumerate(users):
        idx_start = text.index(user)
        try:
            idx_end = text.index(users[i + 1])
        except:
            idx_end = -1

        # Parameters for the RegEx
        dt = '\d\d/\d\d/\d\d\d\d\n'
        num = '\d\d\d\d\d\n'
        val = '.*.\d\d\n'
        key = '\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d'
        superstring = val + dt + num + val + val + key
        k = re.compile(superstring)
        blocks = k.findall(text[idx_start : idx_end])
        
        # Gathering info for each user
        user_block[f'{user}'] = {}
        idx_name = text[ : idx_start - 2].rfind('\n')
        user_block[f'{user}']['name'] = text[idx_name + 1 : idx_start - 1]
        user_block[f'{user}']['invoices'] = blocks

    return user_block

def getKey(text):
    return text[-43 : ]

def getTransactionDate(text):
    r = re.compile('\d\d/\d\d/\d\d\d\d')
    date = r.findall(text)
    return date[0]


def getNfeNumber(text):
    r = re.compile('\d\d\d\d\d\n')
    number = r.findall(text)
    return number[0][ : 5]

def getQuantity(text, number):
    idx_start = text.find(number)
    idx_end = text[idx_start + 6 : ].find('\n')
    return text[idx_start + 6 : idx_start + 6 + idx_end]

    