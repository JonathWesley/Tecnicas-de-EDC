import random

def binarySum(b1, b2, size):
    result = ''
    carry = 0
    for i in range(size-1, -1, -1):
        # soma bit a bit com o carry
        bitResult = carry
        bitResult += 1 if b1[i] == '1' else 0
        bitResult += 1 if b2[i] == '1' else 0
        
        # para bitResult == 2 ou 3 result = 1, caso contrario result = 0
        result = ('1' if bitResult % 2 == 1 else '0') + result
        # para bitResult > 1, carry sera 1
        carry = 0 if bitResult < 2 else 1   

    # caso tenha um carry no fim, soma 1 ao resultado da soma
    if carry !=0: 
        result = binarySum(result, '000000000001', size)

    return result

def bitFlip(b, size):
    result = ''
    for i in range(size):
        if b[i] == '1':
            result += '0'
        else:
            result += '1'
    return result

def verifyCheckSum(b, size):
    for i in range(size):
        if b[i] == '0':
            return False
    return True

def communicationError(b, size):
    result = ''
    bitRand =  random.randint(0,11)
    for i in range(size):
        if i == bitRand:
            if b[i] == '1':
                result += '0'
            else:
                result += '1'
        else:
            result += b[i]
    return result

if __name__ == '__main__':
    size = 12
    
    a = '000000000001'#input("Numero 1: ")
    b = '111111111111'#input("Numero 2: ")
    c = '000000000001'#input("Numero 3: ")
    d = '000000000001'#input("Numero 4: ")
    error = False
    
    result = binarySum(a, b, size)
    result = binarySum(result, c, size)
    result = binarySum(result, d, size)
    
    checkSum = bitFlip(result, size)
    
    ra = a
    rb = b
    rc = c
    rd = d
    
    if error == True:
        wordRand = random.randint(0,3)
        if wordRand == 0:
            ra = communicationError(a, size)
        elif wordRand == 1:
            rb = communicationError(b, size)
        elif wordRand == 2:
            rc = communicationError(c, size)
        else:
            rd = communicationError(d, size)
    
    print(ra)
    
    rResult = binarySum(ra, rb, size)
    rResult = binarySum(rResult, rc, size)
    rResult = binarySum(rResult, rd, size)
    
    finalResult = binarySum(rResult, checkSum, size)
    
    print("Show") if verifyCheckSum(finalResult, size) else print("Tem algo errado ai")
    
    
    
    
    
    
    
    