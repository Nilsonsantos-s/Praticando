frase = input('Digite uma frase qualquer: ')
index = int(input('Digite o index que será removido: '))
first = frase[:index]
last = frase[index+1:]
print(first+last)