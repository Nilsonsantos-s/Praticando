c = int()
copiacontador1 = int()
copiacontador2 = int()
while c < 2:
    c += 1
    contador = int()
    frase = str()
    string = input('Digite uma string qualquer: ')
    while frase != string:
        frase += string[contador]
        contador += 1
    if c == 1:
        copiacontador1 = contador
        copiastring1 = string
    elif c == 2:
        copiacontador2 = contador
        copiastring2 = string
if copiacontador1 > copiacontador2:
    print('Maior String:', copiastring1)
elif copiacontador2 > copiacontador1:
    print('Maior String:', copiastring2)
elif copiacontador1 == copiacontador2:
    print('As duas strings têm tamanhos iguais.')
