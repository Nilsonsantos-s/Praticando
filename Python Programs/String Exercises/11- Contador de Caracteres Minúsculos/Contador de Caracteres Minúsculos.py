string = input('Digite uma string qualquer: ')
tamanho = len(string)
contador = int()
for c in range(0, tamanho):
    letra = string[c]
    letramin = string[c].lower()
    if letra == letramin and letra != ' ':
        contador += 1
print(contador)