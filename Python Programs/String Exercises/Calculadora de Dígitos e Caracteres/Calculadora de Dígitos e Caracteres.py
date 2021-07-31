frase = input('Digite uma frase qualquer: ')
contadornum = 0
contadorstr = 0
for c in frase:
    if c.isnumeric():
        contadornum += 1
    else:
        contadorstr += 1
print('O número de dígitos é {}\nO número de caracteres é: {}'.format(contadornum, contadorstr))