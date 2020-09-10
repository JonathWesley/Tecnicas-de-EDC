# Verifica se eh uma posicao de redundancia
def isRedundantPos(pos, redundantBits):
    for i in range(redundantBits):
        if 2**i == pos:
            return True
    return False

# opt = 0 para calcular hamming no envio
# opt = 1 para calcular a posicao do erro no recebimento
def calculateHamming(hamming, redundantBits, opt):
    kx = ''
    for i in range(redundantBits):
        counter = 0
        # Para todos os bits do vetor
        for j in range(1, (size+1)):
            # Calcula as posições a serem utilizadas para calcular os valores redundantes
            if(j & (2**i) == (2**i)):
                if(hamming[j-1] == '1'):
                    counter += 1
        if opt == 0:
            # se counter for impar, coloca 1 na posicao pn
            if(counter % 2 == 1):
                hamming = hamming[:2**i-1] + '1' + hamming[2**i:]
        else:
            # se counter for impar, valor de kx = 1
            if(counter % 2 == 1):
                kx += '1'
            else:
                kx += '0'
    
    if opt == 0:
        return hamming
    else:
        return kx[::-1]

# verifica se a string passada eh um numero binario
def checkBinary(b):
    s = {'0', '1'} 
    if s == set(b):
        return True
    else: 
        return False
    
# garante o input correto das palavras
def dataInsert(wordName, size):
    r = input(wordName + ": ")
    while len(r) != size or checkBinary(r) == False:   
        print(wordName + " com formato incorreto. Digite novamente.")
        r = input(wordName + ": ")
    return r

if __name__ == '__main__':
    print("Escolha a configuração de Hamming")
    version = int(input("1=(7,4) 2=(12,8) 3=(15,11): "))
    while version < 1 or version > 3:
        print("Digite um numero entre 1 e 3: ")
        version = int(input("1=(7,4) 2=(12,8) 3=(15,11): "))
    
    # Hamming(7,4)
    if version == 1:
        messageSize = 4
        redundantBits = 3
    # Hamming(12,8)
    elif version == 2:
        messageSize = 8
        redundantBits = 4
    # Hamming(15,11)
    else:
        messageSize = 11
        redundantBits = 4
    
    size = messageSize + redundantBits
    message = dataInsert("Palavra", messageSize)
    
    # Coloca os valores do dado em suas respectivas posições
    hamming = ''
    j = 0
    for i in range(size):
        if isRedundantPos(i+1, redundantBits):
            hamming += '0'
        else:
            hamming += message[j]
            j+=1
    
    hamming = calculateHamming(hamming, redundantBits, 0)
    
    print("Palavra enviada: " + hamming)
    
    hamming = dataInsert("Palavra recebida", size)

    errorPosition = calculateHamming(hamming, redundantBits, 1)
    
    null = ''
    for i in range(redundantBits):
        null += '0'
    
    if errorPosition == null:
        print("Mensagem enviada com sucesso.")
    else:
        print("Erro detectado na posição: " + errorPosition)
    