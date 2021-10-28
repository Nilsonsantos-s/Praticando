abertolista = []
fechadolista = []
expressao = input('Digite a expressão: ')
for c in range(0, len(expressao)):
    caractere = expressao[c]
    if caractere == '(':
        abertolista.append(caractere)
    if caractere == ')':
        fechadolista.append(caractere)
if len(abertolista) == len(fechadolista):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
