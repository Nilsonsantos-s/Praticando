lista = [[], []]
for c in range(1,8):
    num = int(input('Digite o {}º número: '.format(c)))
    if c % 2 == 0:
        lista[0].append(num)
    if c % 2 != 0:
        lista[1].append(num)
print('Os valores pares digitados foram: {}'.format(sorted(lista[0])))
print('Os valores ímpares digitados foram: {}'.format(sorted(lista[1])))



