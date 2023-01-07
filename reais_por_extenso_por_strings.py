######## DICIONÁRIO DAS UNiDADES
unidades = {
            '0' : '',
            '1' : 'um', 
            '2' : 'dois', 
            '3' : 'três', 
            '4' : 'quatro', 
            '5' : 'cinco', 
            '6' : 'seis', 
            '7' : 'sete',
            '8' : 'oito', 
            '9' : 'nove',
}
######## DICIONÁRIO DAS DEZENAS
dezenas = {
            '0' : '',
            '10': 'dez', 
            '11': 'onze', 
            '12': 'doze', 
            '13': 'treze', 
            '14': 'quatorze', 
            '15': 'quinze', 
            '16': 'dezesseis', 
            '17': 'dezessete', 
            '18': 'dezoito', 
            '19': 'dezenove',
            '2' : 'vinte', 
            '3' : 'trinta', 
            '4' : 'quarenta', 
            '5' : 'cinquenta', 
            '6' : 'sessenta', 
            '7' : 'setenta', 
            '8' : 'oitenta', 
            '9' : 'noventa' ,            
}
######## DICIONÁRIO DAS CENTENAS
centenas = {'0' : '',
            '1' : 'cento', 
            '2' : 'duzentos' , 
            '3' : 'trezentos' , 
            '4' : 'quatrocentos' , 
            '5' : 'quinhentos' , 
            '6' : 'seiscentos' , 
            '7' : 'setecentos' , 
            '8' : 'oitocentos' , 
            '9' : 'novecentos',
}
######## DICIONÁRIOS DE CONCORDÂNCIA NUMÉRICA PARA AS GRANDEZAS 
conc_mm       = {True: ' milhão' , False: ' milhões' }   
conc_b        = {True: ' bilhão' , False: ' bilhões' }
conc_t        = {True: ' trilhão', False: ' trilhões'}
conc_centavos = {True: ' centavo', False: ' centavos'}


def escrever_por_extenso(numero):    
    sing = False                 
    extenso = ext_c = ext_t = ext_b = ext_mm = ext_m = ext_centavos = '' 
    numero = numero.split('.') # separa os inteiros dos centavos

########### Bloco apenas para escrita dos centavos #############
    if len(numero) > 1:
        centavos = numero[1][:2]
        if len(centavos) == 1:
            centavos += '0'
        sing = True if centavos == '01' else False
        ext_centavos = ' e ' + escrever_centena(centavos) + conc_centavos[sing]
    
########### Bloco para tratamento de valor inteiro #############
    inteiros = numero[0]
    
    if len(inteiros) >= 1 and inteiros != (len(inteiros) * '0'): # verifica se a parte inteira tem valores, senão encerra apenas com o extenso dos centavos
        bloco_c = inteiros[-3:]     # fatia o último bloco de três digitos da string
    else:
        return ext_centavos[3:]
    
########### Tratamento simplificado para o valor de 1 real #############
    if inteiros == '1':
        extenso = 'um real' + ext_centavos
        return extenso
    
########### Bloco para escrita da unidade/dezena/centena #############
    if bloco_c != '000':
        ext_c = escrever_centena(bloco_c)
    
########### Bloco para escrita da unidade/dezena/centena #############
    if len(inteiros) >= 4:          # apenas se o valor for igual ou maior que mil
        bloco_m = inteiros[-6:-3]   # fatia o penultimo bloco de três digitos da string, para milhares
        if bloco_m != '000':
            ext_m = escrever_centena(bloco_m)
            if ext_c == '':
                ext_m += ' mil'
            else:
                ext_m += ' mil e '            

########### Bloco para escrita da unidade/dezena/centena de milhões #############
    if len(inteiros) >= 7:             # apenas se o valor for igual ou maior que milhão
        bloco_mm = inteiros[-9:-6]     # fatia o anti-penúltimo bloco de três digitos da string, para milhões
        if bloco_mm != '000':
            if bloco_mm in ['1', '001']:            # trata a concordância numeral para milhão e milhões
                sing = True
            ext_mm += escrever_centena(bloco_mm)
            if ext_c + ext_m == '':                      # tratamento para encerramento da string, de acordo com o que vem depois
                ext_mm += conc_mm[sing] + ' de'  
            else:
                ext_mm += conc_mm[sing] + ' e '

########### Bloco para escrita da unidade/dezena/centena de bilhões #############
    if len(inteiros) >= 10:            # apenas se o valor for igual ou maior que um bilhão
        bloco_b = inteiros[-12:-9]     # fatia o bloco de três digitos da string correspondente a bilhões
        if bloco_b != '000':
            if bloco_b in ['1', '001']:             # trata a concordância numeral
                sing = True
            ext_b += escrever_centena(bloco_b)
            if ext_c + ext_m + ext_mm == '' :             # tratamento para encerramento da string, de acordo com o que vem depois
                ext_b += conc_b[sing] + ' de'
            else:
                ext_b += conc_b[sing] + ' e '

########### Bloco para escrita da unidade/dezena/centena de trilhões #############
    if len(inteiros) >= 13:             # apenas se o valor for igual ou maior que um trilhão
        bloco_t = inteiros[-15:-12]     # fatia o bloco de três digitos da string correspondente a trilhões   
        if bloco_t != '000':
            if bloco_t in ['1', '001']:             # trata a concordância numeral
                sing = True
            ext_t += escrever_centena(bloco_t)                                         
            if ext_c + ext_m + ext_mm + ext_b == '' :    # tratamento para encerramento da string, de acordo com o que vem depois
                ext_t += conc_t[sing] + ' de'
            else:
                ext_t += conc_t[sing] + ' e '


    bloco_b = inteiros[-12:-9] if len(inteiros) >= 10 else ''   
    bloco_t = inteiros[-15:-12] if len(inteiros) >= 13 else ''    
    
    extenso = ext_t + ext_b  + ext_mm + ext_m + ext_c + ' reais' + ext_centavos
    return extenso

def escrever_centena(numeral):
    ext = ''    
    tamanho = len(numeral)
    if tamanho == 3:    
        if numeral == '100':  # tratando o "cem" / "cento" para a centena
            ext += 'cem' 
        else:
            ext += centenas[numeral[0]]
            
    if tamanho >= 2:
        if numeral[-2:] != '00' and numeral[-3:-2] != '0' and tamanho == 3: # verifica se tem numeros acima de zero depois, se tiver, concatena o "e" ...
            ext += ' e '                                                    #... obs. isso só ocorre em blocos completos de 3 digitos por isso a verificação também do tamanho
                    
        if numeral[-2] == '1':             # verfiica se o numero está entre 10 e 19, devido a diferença no padrão de escrita desses números
            ext += dezenas[numeral[-2:]]
            return ext                     # caso a dezena seja menor que 20, o sistema retorna, pois a unidade já esté implicita na escrita do número
        else:
            ext += dezenas[numeral[-2]]

        if numeral[-2] not in '10' and numeral[-1] != '0': # caso a dezena não seja '0' nem '1' e nem a unidade seja '0', adiciona um 'e' à string ext
             ext += ' e '
    
    ext += unidades[numeral[-1]] 
    
    return ext   

num = str(input('Digite um valor em reais R$: ').replace(',', '.'))
print(escrever_por_extenso(num))
