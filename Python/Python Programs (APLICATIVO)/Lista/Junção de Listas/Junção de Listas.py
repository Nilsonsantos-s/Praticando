lista1 = []
lista2 = []
lista3 = []
print('='*50)
nelementos = int(input('Digite o número de elementos da primeira lista: '))
for c in range(1, nelementos+1):
    numero = int(input('Digite um número: '))
    lista1.append(numero)
print('='*30)
nelementos = int(input('Digite o número de elementos da segunda lista: '))
for c in range(1, nelementos+1):
    numero = int(input('Digite um número: '))
    lista2.append(numero)
print('='*30)
lista3 = lista1 + lista2
lista3.sort()
print('A nova lista em ordem é:', lista3)

