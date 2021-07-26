frase = input('Digite uma frase: ')
fraseinvertida = frase.replace(' ', '')[::-1]
if fraseinvertida == frase.replace(' ', ''):
    print('A frase invertida é: {}\nÉ um palíndromo.'.format(fraseinvertida))
else:
    print('A frase invertida é: {}\nNão é um palíndromo.'.format(fraseinvertida))
