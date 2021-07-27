frase = input('Digite uma frase qualquer: ')
contador = int()
while True:
    contador += 1
    copiafrase = frase[0:contador]
    if copiafrase == frase:
        break
print(f'O número de caracteres (tamanho) é igual a: {contador}')
