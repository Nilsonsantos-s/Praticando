def leiaint(frase):
    n = input(frase)
    while True:
        resultado = n.isnumeric()
        if resultado:
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
            n = input(frase)
    n = int(n)
    return n


##Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

