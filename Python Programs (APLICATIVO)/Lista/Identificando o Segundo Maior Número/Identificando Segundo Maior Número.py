lista = []
for c in range(1,6):
    numero = int(input('Digite um número: '))
    lista.append(numero)
print('A lista é:', lista)
maior = []
for c in range(0, len(lista)):
    if c > 0:
        if lista[c] > lista[c-1]:
            maior.append(lista[c])
target = maior[len(maior)-1]
print('O segundo maior número é:', target)
            
