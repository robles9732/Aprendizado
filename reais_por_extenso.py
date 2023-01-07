numerais = {
            1:   'um', 
            2:   'dois', 
            3:   'três', 
            4:   'quatro', 
            5:   'cinco', 
            6:   'seis', 
            7:   'sete',
            8:   'oito', 
            9:   'nove',
            10:  'dez', 
            11:  'onze', 
            12:  'doze', 
            13:  'treze', 
            14:  'quatorze', 
            15:  'quinze', 
            16:  'dezesseis', 
            17:  'dezessete', 
            18:  'dezoito', 
            19:  'dezenove', 
            20:  'vinte', 
            30:  'trinta', 
            40:  'quarenta', 
            50:  'cinquenta', 
            60:  'sessenta', 
            70:  'setenta', 
            80:  'oitenta', 
            90:  'noventa' ,
            100: ('cem', 'cento') , 
            200: 'duzentos' , 
            300: 'trezentos' , 
            400: 'quatrocentos' , 
            500: 'quinhentos' , 
            600: 'seiscentos' , 
            700: 'setecentos' , 
            800: 'oitocentos' , 
            900: 'novecentos',            
            1000: 'mil',
            101 : ('milhão', 'milhões'),
            102:  ('bilhão', 'bilhões'),
            103:  ('trilhão', 'trilhões')
}

def escrever_centenas(numero):        
    
    bloco_cem = ''    
        
    centena = numero // 100 * 100
    if centena > 0:        
        if centena > 100:
            bloco_cem += numerais[centena]
        else:
            if numero == 100:                
                bloco_cem += numerais[centena][0]
            else:
                bloco_cem += numerais[centena][1]
        numero -= centena
        if numero > 0:
            bloco_cem += ' e '
    
    dezena = numero // 10 * 10 
    if dezena >= 20:    
        bloco_cem += numerais[dezena]         
        numero -= dezena
        if numero > 0:
            bloco_cem += ' e '
    elif dezena > 0:
        bloco_cem += numerais[numero]
        numero = 0
    
    if numero > 0:
       bloco_cem += numerais[numero]

    return bloco_cem

def escrever_por_extenso(numero):
    inteiro = int(numero)
    centavos = round(numero - inteiro, 2) * 100        
    ext = ''
    
    if inteiro == 1:
        ext = numerais[inteiro] + ' ' + 'real'
        return ext
    
    if inteiro >= 1000000000000:
        trilhao = inteiro // 1000000000000
        if trilhao == 1:
            i = 0    
        else:
            i = 1
        ext += escrever_centenas(trilhao) + ' ' + numerais[103][i]        
        inteiro -= trilhao * 1000000000000
        if inteiro > 0:
            ext += ' e '

    if inteiro >= 1000000000:
        bilhao = inteiro // 1000000000
        if bilhao == 1:
            i = 0    
        else:
            i = 1
        ext += escrever_centenas(bilhao) + ' ' + numerais[102][i]        
        inteiro -= bilhao * 1000000000
        if inteiro > 0:
            ext += ' e '

    if inteiro >= 1000000:
        milhao = inteiro // 1000000
        if milhao == 1:
            i = 0    
        else:
            i = 1
        ext += escrever_centenas(milhao) + ' ' + numerais[101][i]        
        inteiro -= milhao * 1000000
        if inteiro > 0:
            ext += ' e '

    
    if inteiro >= 1000:
        milhar = inteiro // 1000
        ext += escrever_centenas(milhar) + ' mil'
        inteiro -= milhar * 1000
        if inteiro > 0:
            ext += ' e '
    
    ext += escrever_centenas(inteiro) + ' reais'
    
    if centavos > 0:        
        ext += ' e ' + escrever_centenas(centavos)
        
        if centavos > 1:
            str_centavo = ' centavos'
        else:
            str_centavo = ' centavo'
        
        ext += str_centavo
    
    print(ext)

num = float(input('Digite um valor em reais R$: ').replace(',', '.'))
escrever_por_extenso(num)
