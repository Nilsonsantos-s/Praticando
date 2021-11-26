lista = []
for c in range(1,6):
    numero = int(input('Digite um número: '))
    lista.append(numero)
for c in range(0, len(lista)):
    if c > 0:
        if lista[c] > lista[c-1]:
            maior = lista[c]
print('A lista é:', lista)
print('O maior número é:', maior)