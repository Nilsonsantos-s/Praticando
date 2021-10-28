tupla = 1, 2, 3, 4, 5
numero = int(input('Digite o ítem que deseja remover: '))
if numero in tupla:
    None
else:
    while True:
        print('Digite um ítem válido')
        numero = int(input('Digite o ítem que deseja remover: '))
        if numero in tupla:
            break
posicao = tupla.index(numero)
tupla = tupla[0:numero-1] + tupla[numero:]
print(tupla)