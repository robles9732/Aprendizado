from random import choice

matriz_1 = [[],[],[]] # matriz que armazena os números da linhas e das colunas
matriz_2 = [[],[],[]] # matriz auxiliar para liberar a matriz_1 
grande_lista = [] # lista de número que transpõe a matriz 1 em uma única linha 
escolha = 0 # contador para encerrar o programa
num_escolhido = 0 # o número do resultado

# Gera a tabela inicial do jogo
x = 0 # armazenará o número sorteado de uma lsita
lista_numeros = list(range(1, 22)) # lista de 1 a 21 que fornecerá os números para o choice
selecao = [] # lista para popular as colunas da tabela

while len(selecao) < 21: # repete o soreio até que a lista seleção tenha todos os números
    x = choice(lista_numeros)    # usa seleção aleatória a partir da lista
    if x not in selecao:  # se não tiver o número selecionado, para evitar duplicação dos valores
        selecao.append(x)  # adiciona o número selecionado
matriz_2[0] = selecao[:7]  # fatia a lista com 21 números em 3, criando uma matriz (3, 7) e...
matriz_2[1] = selecao[7:14] # ... armazena na matriz auxiliar
matriz_2[2] = selecao[14:]

while escolha < 3:  # após 3 escolhas do jogador, esse número de vezes é necessária para a transposição correta do número selecionado
    
    print()  
    print('---------------')  #
    print('  A |  B |  C |')  # cabeçalho da tabela
    print('---------------')  #
    matriz_1 = matriz_2[:]  # armazena os valores da matriz auxilar na matriz de números
    for i in range (7):   # iterações para imprimir as linhas    
        for j in range(3):            
            print(f' {matriz_1[j][i]:2} |', end='')  # i gera as colunas e k as linhas
        print()
    print('---------------') # rodapé da tabela
    print()                  
       
    coluna =  input(str('Digite a coluna em que está seu número [A] [B] [C] |X para sair|: ' ))[0].strip() # captura a escolha do jogador
    if coluna in 'aA':    # se for "A" armazena em 1 na variável a, os outros passam a ser indiferentes
        a = 1
        b = 0
        c = 2
    elif coluna in 'bB': # se for "B", a variável b ganha o número 1
        a = 0
        b = 1
        c = 2
    elif coluna in 'cC': # se for "c", a variável c ganha o número 1
        a = 0
        b = 2
        c = 1
    elif coluna in 'xX': # opção pra quem quer arregar
        break
    else:                # caso não tenha sido digitado nenhum dos valores desejados
        print()
        print(f'{coluna.upper()} NÃO É UMA OPÇÂO VÁLIDA!!!')        # apresenta a mensagem e ...
        continue                                                    # ... volta para o início do looping
    matriz_1[a] = matriz_2[0]    # até aqui, matriz_1 e matriz_2 eram idênticas, agora a matriz 1 passa a ter ...
    matriz_1[b] = matriz_2[1]    # suas colunas reorganizadas, de forma que a coluna com o número escolhido sempre fique ...
    matriz_1[c] = matriz_2[2]    # ... no meio

    for k in range(3):   # itera pelas colunas da matriz
        for m in range(7): # para cada coluna, itera pelas linhas 
            grande_lista.append(matriz_1[k][m])  # para cada iteração, o número da tabela é colocada linha a linha em uma única lista
    
    g = 0 # variável para iteração na Grande Lista 
    while g <= 20:        # intera com a grande lista até que tenha lido todos os valores
        for n in range(7):   # itera entre as colunas ...
            for o in range(3):  # ... e linhas da Matriz Auxiliar
                matriz_2[o][n] = grande_lista[g] # ...populando-a com os números da Grande Lista, gerando uma matriz transposta
                g += 1   # aumenta o contador                             
                  
    print() 
    num_escolhido = grande_lista[10]  # o número escolhido vai para a 11.a posição Grande Lista após 3 iterações, como a Grande Lista é apagada a cada looping ...    
    grande_lista.clear()              # ... na última iteração ficarrá armazenado na verável num_escolhe que será apresentada fora do laço
    escolha += 1

print(f'O número escollhido foi {num_escolhido}')  # apresenta o último valor escolhido armazenado ao final de 3 iterações
print()   