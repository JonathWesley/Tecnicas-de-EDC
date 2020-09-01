def isRedundantPos(pos, redundantBits):
    for i in range(redundantBits):
        if 2**i == pos:
            return True
    return False

#criar funcao pra cagar o hamming

if __name__ == '__main__':
    version = 1
    
    # Hamming(7,4)
    if version == 0:
        messageSize = 4
        redundantBits = 3
    # Hamming(12,8)
    elif version == 1:
        messageSize = 8
        redundantBits = 4
    # Hamming(15,11)
    else:
        messageSize = 11
        redundantBits = 4
    
    size = messageSize + redundantBits
    message = '10101010' #input("Dado: ")
    
    # Coloca os valores do dado em suas respectivas posições
    hamming = ''
    j = 0
    for i in range(size):
        if isRedundantPos(i+1, redundantBits):
            hamming += '0'
        else:
            hamming += message[j]
            j+=1
            
    # Coloca os valores da paridade
    step = 2
    neighbors = 1
    print(hamming)
    
    # Para todos os bits redundantes (p1p2p4p8...)
    for i in range(redundantBits):
        counter = 0
        # Para todos os bits do vetor
        for j in range(1, (size+1)):
            # Calcula as posições a serem utilizadas para calcular os valores redundantes
            if(j & (2**i) == (2**i)):
                if(hamming[j-1] == '1'):
                    counter += 1
        if(counter % 2 == 1):
            hamming = hamming[:2**i-1] + '1' + hamming[2**i:]
    print(hamming)
    
    hamming ="111101001010"

    problemDetector =''
    # to vendo meio dobrado fei
    # Para todos os bits redundantes (p1p2p4p8...)
    for i in range(redundantBits):
        counter = 0
        # Para todos os bits do vetor
        for j in range(1, (size+1)):
            # Calcula as posições a serem utilizadas para calcular os valores redundantes
            if(j & (2**i) == (2**i)):
                if(hamming[j-1] == '1'):
                    counter += 1
        if(counter % 2 == 1):
            problemDetector += '1'
        else:
            problemDetector += '0'
    print(problemDetector[::-1])
    
    
    
    
    
    