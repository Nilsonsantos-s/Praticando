def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')

##Programa Principal
x = input('Nome do Jogador: ')
y = input('Número de Gols: ')
if x.strip() == '':
    if y.strip() == '':
        ficha(gols=0)
    else:
        ficha(gols=y)
else:
    if y.strip() == '':
        ficha(x, gols=0)
    else:
        y = int(y)
        ficha(x, gols=y)
