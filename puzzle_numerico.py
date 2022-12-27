import sys as s
import numpy as np
from random import choice

matriz = np.arange(1,17).reshape(4, 4) #cria a matriz numpy
matriz[3][3] = 0
gabarito = np.arange(1,17).reshape(4, 4) #cria a matriz numpy
gabarito[3][3] = 0
x, y = np.where(matriz == 0) #maneira de trazer as coordenadas de 0
    
direcao = [0, 1, 2, 3]

for _ in range(3000):   # função que randomiza a tabela inicial
    movimento = choice(direcao) 
    
    if movimento == 0:
        
        if x - 1 >= 0:       
            matriz[x,y] = matriz[x - 1, y]  
            matriz[x-1,y] = 0     
            x -= 1 
    if movimento == 1:        
        if x + 1 <= 3:            
            matriz[x,y] = matriz[x + 1, y]
            matriz[x + 1, y] = 0
            x += 1  
    if movimento == 2:
        if y - 1 >= 0:            
            matriz[x,y] = matriz[x, y - 1]
            matriz[x, y - 1] = 0
            y -= 1
    if movimento == 3:    
        if y + 1 <= 3:            
            matriz[x,y] = matriz[x, y + 1]
            matriz[x, y + 1] = 0
            y += 1


print('**************************************************************')
print('O objetivo é mover os números de modo que fiquem na sequência. Só é possível trocar de posição com o Zero, tanto para cima, quanto para baixo, ele é seu "espaço vazio"')
print('O zero deve ficar na última posição, ele será promovido ao número 16 e você ganha a partida')
print('')
print('Aviso de antemão que a jogabilidade é horrível!')
print()
print('                      Cima')
print('                      [W]')
print('         Esquerda [A]     [D] Direita')
print('                      [S]')
print('                     Baixo')
print()
print('         [Enter]:Confirma o movimento')
print()
print('**************************************************************')
input('Começar!')
print()
while True:

    print('----------------')
    
    for i in range(4):          # imprime o layout da matriz na tela
        for j in range(4):
            print(f'{matriz[i, j]:2} |', end = '' )                 
        print()    
        print('----------------')   
    
    if matriz[3,3]==16: # o número 16 só aparece quando o jogador ordena toda a matriz, então o jogo se encerra
        print()
        print('***********************************************************')
        print('* Parabéns, você merece aplausos por finalizar esse jogo! *')
        print('***********************************************************')
        s.exit(0)
        print()
    
    try:
       selecao = (input('Escolha a direção que deseja mover o Zero ([X] para Sair: ) '))[0].strip()  
    except:
       if IndexError:   # Contrloe de erro para o caso do jogador apertar o enter
           continue       

    if selecao in 'wW':     # faz o movimento para cima, tocando o Zero de posição com o número imediatamente acima
        if x - 1 >= 0:       # verifica se há espaço acima
            matriz[x,y] = matriz[x - 1, y]  # faz a troca dos valores das células
            matriz[x-1,y] = 0               #
            x -= 1          # atualiza a corrdenada do Zero
        else:            # se chegar no limite superior da matriz
            print()
            print('Ops! Bateu no teto!')
        
    elif selecao in 'sS':    # faz o movimento para baixo e repete a mesma lógica do movimento para Cima
        if x + 1 <= 3:            
            matriz[x,y] = matriz[x + 1, y]
            matriz[x + 1, y] = 0
            x += 1  
        else:              
            print()
            print('Você não é o Chewbacca mas encontrou o solo')        
        
    elif selecao in 'aA':     # faz o movimento para a Esquerda e repete a mesma lógica do movimento para Cima
        if y - 1 >= 0:            
            matriz[x,y] = matriz[x, y - 1]
            matriz[x, y - 1] = 0
            y -= 1
        else:            
            print()
            print('Tudo tem limite, até a tela do seu computador')        
        
    elif selecao in 'dD':   # faz o movimento para a Direita e repete a mesma lógica do movimento para Cima
        if y + 1 <= 3:            
            matriz[x,y] = matriz[x, y + 1]
            matriz[x, y + 1] = 0
            y += 1
        else:            
            print()
            print('You not shall pass!')        
        
    elif selecao in 'xX':
        print()
        print('Até mais, desculpa qualquer coisa!')        
        print()
        s.exit()    
    else:
        print()
        print('Não entendi!')
        print()
    

    if np.array_equal(matriz, gabarito):
        matriz[3,3] = 16
