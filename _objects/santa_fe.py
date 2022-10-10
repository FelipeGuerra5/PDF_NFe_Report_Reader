def getDataSantaFe(obj):
    pass

    print('[GETING DATA FROM SANTA FE]')
    print(obj)

    
    data = {}
    
    data['key'] = getKey(obj.text)
    data['farmer'] = getFarmer(obj.text)
    data['date_of_transaction'] = getTransaction(obj.text)
    data['farmer_cpf'] = getCpf(obj.text)
    data['nfe_number'] = getNfeNumber(obj.text)

# Methods for extracting the data from text
def getKey(text):
    pass
def getFarmer(text):
    pass
def getTransaction(text):
    pass
def getCpf(text):
    pass
def getNfeNumber(text):
    pass