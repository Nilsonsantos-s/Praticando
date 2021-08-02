lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
         'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
copialetra = ''
for c1 in lista:
    print('Na palavra {} temos as vogais:'.format(c1.upper()), end='')
    palavra = c1
    for c2 in range(0, len(palavra)):
        letra = palavra[c2]
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            copialetra = copialetra + ' ' + letra
    print(copialetra)
    copialetra = ''

