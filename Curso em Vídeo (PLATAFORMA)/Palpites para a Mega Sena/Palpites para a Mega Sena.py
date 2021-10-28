import random
print('-'*30)
print('{: ^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
numjogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print('-'*11, 'SORTEANDO 4 JOGOS', '-'*11)
lista = []
contador = 0
for c in range(1, numjogos+1):
    lista.append([])
for c in range(0, numjogos):
    for c2 in range(1, 7):
        naleatorio = random.randint(0, 60)
        lista[c].append(naleatorio)
for c in range(0, numjogos):
    contador += 1
    print(end='Jogo {}: ['.format(contador))
    for c2 in range(0, 6):
        if c2 == 5:
            print('{:]^3} '.format(lista[c][c2]), end='')
        else:
            print('{:^3} - '.format(lista[c][c2]), end='')
    print()
