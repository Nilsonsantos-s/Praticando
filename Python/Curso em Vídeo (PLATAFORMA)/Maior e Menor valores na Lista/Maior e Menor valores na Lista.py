lista = []
for contador in range(1,6):
    num = int(input('Digite o {}º valor: '.format(contador)))
    if contador == 1:
        maior = num
        menor = num
    if contador > 1:
        if num > maior:
            maior = num
            if num == num:
                posigual = contador-1
        elif num < menor:
            menor = num
    lista.append(num)
print('Você digitou os valores:', lista)
print('O maior valor digitado foi {} nas posições '.format(maior), end='')
for pos, item in enumerate(lista):
    if item == maior:
        print(pos, end= '... ')
print('')
print('O menor valor digitado foi {} nas posições '.format(menor), end='')
for pos, item in enumerate(lista):
    if item == menor:
        print(pos, end= '... ')