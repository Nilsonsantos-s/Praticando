contador = int(10)
while True:
    if contador == 10:
        num = int(input('Quer ver a tabuada de qual valor?: '))
        contador = 0
    else:
        if num < 0:
            break
        if contador < 10:
            contador = contador + 1
            print(f'{num} * {contador} = {num*contador}')
print('PROGRAMA ENCERRADO. VOLTE SEMPRE!')

