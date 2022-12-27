import numpy as np
import sys as s

matriz = np.arange(1,22).reshape(3, 7) 
np.apply_along_axis(np.random.shuffle, 1, matriz) # randomiza a matriz por linha
np.apply_along_axis(np.random.shuffle, 0, matriz) # randomiza a matriz por colun
matriz = np.transpose(matriz).reshape(7,3)
escolha = 0
num_escolhido = 0

while escolha < 3:  
    
    print()  
    print('---------------')  
    print('  A |  B |  C |')  
    print('---------------') 
    
    for i in range (7):   
        for j in range(3):            
            print(f' {matriz[i][j]:2} |', end='') 
        print()
    print('---------------') 
    print()                  
    
    coluna =  input(str('Digite a coluna em que está seu número [A] [B] [C] |X para sair|: ' ))[0].strip() # captura a escolha do jogador
    
    if coluna in 'aA':    
        pos = [1, 0, 2]
    
    elif coluna in 'bB':
        pos = [0, 1, 2]

    elif coluna in 'cC':
        pos = [0, 2, 1]
    
    elif coluna in 'xX':
        s.exit()
    
    else:                
        print()
        print(f'{coluna.upper()} NÃO É UMA OPÇÂO VÁLIDA!!!')       
        continue                                                    
    matriz[:,[0, 1, 2]] = matriz[:, pos]    
    
    matriz = np.transpose(matriz).reshape(1,21)
    num_escolhido = matriz[0][10]   
    matriz = np.transpose(matriz).reshape(7,3)        
    escolha += 1

print('==================================')
print(f'*  O número escollhido foi o {num_escolhido}  *')
print('==================================') 
print()
s.exit()