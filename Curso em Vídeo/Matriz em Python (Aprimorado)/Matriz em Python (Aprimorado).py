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
somapar = 0
somater = 0
listasegunda = []
for c in range(0, 9):
    contador += 1
    print('[ {:^5} ]'.format(lista[x][y]), end='')
    if lista[x][y] % 2 == 0:
        somapar += lista[x][y]
    if y == 2:
        somater += lista[x][y]
    if x == 1:
        listasegunda.append(lista[x][y])
    if contador % 3 == 0:
        print('')
        x += 1
    y += 1
    if y == 3:
        y = 0
for num in listasegunda:
    maiorseg = num
    if num > maiorseg:
        maiorseg = num
print('A soma de todos números pares é:', somapar)
print('A soma dos números da terceira coluna é:', somater)
print('O maior valor da segunda linha é:', maiorseg)
