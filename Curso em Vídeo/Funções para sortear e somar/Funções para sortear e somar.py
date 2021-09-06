numeros = []
def sorteia():
    from time import sleep
    from random import randint
    print('Os números sorteados são:', end=' ')
    for c in range(1, 6):
        num = randint(0, 9)
        print(num, end=' ')
        sleep(0.50)
        numeros.append(num)
def somaPar():
    somapares = 0
    for copianum in numeros:
        if copianum % 2 == 0:
            somapares += copianum
    print()
    print(f'A soma de todos os números pares é igual a {somapares}!')
#Programa Principal
sorteia()
somaPar()

