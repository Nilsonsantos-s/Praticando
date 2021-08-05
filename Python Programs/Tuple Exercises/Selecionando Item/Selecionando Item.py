numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
posicao = int(input('Digite um número de 0 a 8: '))
if posicao > 8 or posicao < 0:
    while True:
        posicao = int(input('Tente novamente. Digite um número de 0 a 8: '))
        if posicao <= 8 and posicao >= 0:
            break
print('O número selecionado é:', numeros[posicao])

