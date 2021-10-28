frase = input('Digite uma frase: ')
tamanho = len(frase)
contador = int()
for c in range(0, tamanho):
    letra = frase[c].lower()
    resposta = letra in 'a, e, i, o, u'
    resposta = str(resposta)
    if resposta == 'True':
        contador += 1
print('O número de vogais é: ', contador)
