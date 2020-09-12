# retorna o resultado de uma xor entra 2 palavras de mesmo tamanho
def xor(a, b):
    result = ''
    for i in range(len(a)):
        bSum = int(a[i]) + int(b[i])
        if bSum == 1:
            result += '1'
        else:
            result += '0'
    return result

# remove todos os zeros a esquerda de uma palavra
def removeZeros(data):
    for i in range(len(data)):
        if data[i] == '1':
            return data[i:]
    return '000'

# retorna o resto da divisao de data por crc
def remainder(data, crc):
    # remove os zeros a direta de data
    dataAux = removeZeros(data)
    
    # se a palavra for menor que 4, nao tem mais como dividir
    if len(dataAux) < 4:
        return dataAux
    
    # xor entre os 4 bits a direita de data com crc
    resultXor = xor(dataAux[:4], crc)
    # junta o resultado da xor com os ultimos digitos de data
    result = resultXor + dataAux[4:]
    # faz mais uma divisao
    return remainder(result, crc)
    
# verifica se a string passada eh um numero binario
def checkBinary(b):
    for i in range(len(b)):
        if b[i] != '0' and b[i] != '1':
            return False
    return True
    
# garante o input correto das palavras
def dataInsert(wordName, size):
    r = input(wordName + ": ")
    while len(r) != size or checkBinary(r) == False:   
        print(wordName + " com formato incorreto. Digite novamente.")
        r = input(wordName + ": ")
    return r

def verifyZero(b):
    s = {'0'} 
    if s == set(b):
        return True
    else: 
        return False
    
if __name__ == '__main__':
    data = dataInsert("Palavra", 11)
    crc = dataInsert("CRC", 4)
    
    msgSent = data
    
    # adiciona os bits de CRC
    data += '000'
    
    rest = remainder(data, crc)
    
    result = ''
    cont = len(rest)
    while cont < 3:
        result += '0'
        cont += 1
    result += rest
    
    print("Paridade: " + result[-3:])
    msgSent += result[-3:]
    print("Mensagem enviada: " + msgSent)
    
    msgReceived = dataInsert("Palavra recebida", 14)
    
    rest = remainder(msgReceived, crc)
    
    print("Resto de verificação: " + result[-3:])
    
    print("Mensagem recebida corretamente.") if verifyZero(result) == True else print("Falha detectada.")
    