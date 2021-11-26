alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
	 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
string = input('Digite uma string qualquer: ')
string = string.lower()
letra = str()
for c1 in range(0, len(string)):
    stringemalfabeto= str(string[c1] in alfabeto)
    if stringemalfabeto == 'True':
        resultado = str(string[c1] in letra)
        if resultado == 'False':
            letra += string[c1]
resposta2 = str()
for c2 in range(0, len(letra)):
    resposta1 = str(letra[c2] in alfabeto)
    resposta2 = resposta2 + resposta1 + ' '
resultado2 = str('False' in resposta2)
if resultado2 == 'False' and len(letra) == 26:
    print('É um pangrama')
else:
    print('Não é um pangrama')