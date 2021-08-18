x = 0
y = 0
lista = [[], [], []]
for c in range(1,10):
    valor = int(input('Digite um valor para [{}, {}]: '.format(x, y)))
    if x == 0:
        lista[0].append(valor)
    elif x == 1:
        lista[1].append(valor)
    elif x == 2:
        lista[2].append(valor)
    if c % 3 == 0:
        x += 1
    y += 1
    if y == 3:
        y = 0
x = 0
y = 0
contador = 0
for c in range(0, 9):
    contador += 1
    print('[ {:^5} ]'.format(lista[x][y]), end='')
    if contador % 3 == 0:
        print('')
        x += 1
    y += 1
    if y == 3:
        y = 0