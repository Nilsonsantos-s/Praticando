from random import randint
lista = []
elementos = int(input('\033[1;35mDigite o número de elementos: \033[m'))
for contador in range(1, elementos+1):
    lista.append(randint(1, 20))
for número in lista:
    print(f'\033[1;33m{número}', end=' ')