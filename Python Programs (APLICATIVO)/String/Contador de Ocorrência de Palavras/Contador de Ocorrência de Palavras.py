frase = input('Digite uma frase qualquer: ')
palavra= input('Digite uma palavra da string: ')
nocorrenciacopia = '0'
lista = frase.split()
for c in range(0, len(lista)):
    nocorrencia= lista.count(lista[c])
    palavracopia = lista[c]
    if palavracopia == palavra:
        nocorrenciacopia = nocorrencia
print('Número de ocorrências:', nocorrenciacopia)
