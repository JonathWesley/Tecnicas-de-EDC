import random

# realiza a soma de dois numeros binarios de mesmo tamanho
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
        carryWord = '0'
        for i in range(size-2):
            carryWord += '0'
        carryWord += '1'
        result = binarySum(result, carryWord, size)

    return result

# percorre a palavra invertendo todos os bits
def bitFlip(b, size):
    result = ''
    for i in range(size):
        if b[i] == '1':
            result += '0'
        else:
            result += '1'
    return result

# percorre toda a palavra e verifica se existe algum 0
def verifyCheckSum(b, size):
    for i in range(size):
        if b[i] == '0':
            return False
    return True

# insere uma inversao de bits em uma posicao aleatoria da palavra
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

# verifica se a string passada eh um numero binario
def checkBinary(b):
    for i in range(len(b)):
        if b[i] != '0' and b[i] != '1':
            return False
    return True

# garante o input correto das palavras
def dataInsert(n, size):
    r = input("Palavra " + n + ": ")
    while len(r) != size or checkBinary(r) == False:   
        print("Palavra com formato incorreto. Digite novamente.")
        r = input("Palavra " + n + ": ")
    return r
    

if __name__ == '__main__':
    size = 12 # tamanho das palavras
    
    a = dataInsert('1', size)
    b = dataInsert('2', size)
    c = dataInsert('3', size)
    d = dataInsert('4', size)
    
    result = binarySum(a, b, size)
    result = binarySum(result, c, size)
    result = binarySum(result, d, size)
    
    checkSum = bitFlip(result, size)
    print("\nPalavra de paridade(checksum): " + checkSum)
    
    
    error = input("Deseja inverter um bit? S/N: ")
    while error != "S" and error != "s" and error != "N" and error != "n":
        print("Entrada incorreta, digite novamente.")
        error = input("Deseja inverter um bit? S/N")
    
    ra = a
    rb = b
    rc = c
    rd = d
    
    if error == 'S' or error == 's':
        wordRand = random.randint(0,3)
        if wordRand == 0:
            ra = communicationError(a, size)
        elif wordRand == 1:
            rb = communicationError(b, size)
        elif wordRand == 2:
            rc = communicationError(c, size)
        else:
            rd = communicationError(d, size)
    
    print("\nMensagem Recebida: ")
    print("A: " + ra)
    print("B: " + rb)
    print("C: " + rc)
    print("D: " + rd)
    print("CheckSum: " + checkSum + "\n")
    
    rResult = binarySum(ra, rb, size)
    rResult = binarySum(rResult, rc, size)
    rResult = binarySum(rResult, rd, size)
    print("Soma das palavras: " + rResult)
    
    finalResult = binarySum(rResult, checkSum, size)
    print("Soma de ambos checksums: " + finalResult)
    
    print("Mensagem recebida corretamente.") if verifyCheckSum(finalResult, size) else print("Falha no CheckSum.")
    