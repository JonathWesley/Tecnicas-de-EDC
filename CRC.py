def xor(a, b):
    result = ''
    for i in range(len(a)):
        bSum = int(a[i]) + int(b[i])
        if bSum == 1:
            result += '1'
        else:
            result += '0'
    return result

def removeZeros(data):
    for i in range(len(data)):
        if data[i] == '1':
            return data[i:]
    return '0000'

def binaryDivision(data, crc):
    dataAux = removeZeros(data)
    resultXor = xor(dataAux[:4], crc)
    result = resultXor + dataAux[4:]
    if len(result) <= 4:
        return result
    else:
        return binaryDivision(result, crc)
    
if __name__ == '__main__':
    data = '10101010'#input("Dado: ")
    crc = '1110'#input("CRC: ")
    
    msgSent = data
    
    data += '000'
    
    rest = binaryDivision(data, crc)
    
    msgSent += rest[-3:]

    print("Mensagem enviada: " + msgSent)
    
    msgReceived = '10101010010'#input("Mensagem recebida: ")
    
    rest = binaryDivision(msgReceived, crc)
    
    print("Show") if rest[-3:] == '000' else print("Algo de errado nao esta certo")