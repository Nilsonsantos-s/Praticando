nome = input('Nome do Jogador: ')
npartidas = int(input(f'Quantas partidas {nome} jogou?: '))
dados = {'Nome': nome}
listagols = []
listapar = []
total = 0
for c in range(0, npartidas):
    listapar.append(c)
    gol = int(input(f'Quantos gols na partida {c}?: '))
    total = total + gol
    listagols.append(gol)
dados['Gols'] = listagols
dados['Total'] = total
print('=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 40)
dados['Partidas'] = listapar
print(f'O jogador {nome} jogou {npartidas} partidas')
for c in range(0, npartidas):
    print(f'    => Na partida {dados["Partidas"][c]}, fez {dados["Gols"][c]} gols')
print(f'Foi um total de {dados["Total"]} gols.')