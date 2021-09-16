lista = []
while True:
    nome = input('Nome do Jogador: ')
    npartidas = int(input(f'Quantas partidas {nome} jogou?: '))
    dados = {'Nome': nome}
    listagols = []
    listapar = []
    total = 0
    for c in range(0, npartidas):
        listapar.append(c)
        gol = int(input(f'Quantos gols na partida {c+1}?: '))
        total = total + gol
        listagols.append(gol)
    dados['Gols'] = listagols
    dados['Total'] = total
    resposta = input('Quer continuar? [S/N]: ')
    resposta = resposta.lower()
    lista.append(dados)
    if resposta != 'n' and resposta != 's':
        while True:
            print('Digite uma opção válida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta = resposta.lower()
            if resposta == 'n' or resposta == 's':
                break
    if resposta == 'n':
        break
contador = 0
print('Cod Nome     Gols                Total')
print('-' * 40)
for pessoa in lista:
    print('{} {:<10} {:<15} {:^10}'.format(contador, pessoa["Nome"], str(pessoa["Gols"]), pessoa["Total"]))
    contador += 1
print('-' * 40)
resposta = 0
while True:
    resposta = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if resposta >= 0 and resposta < len(lista):
        None
    else:
        while True:
            if resposta == 999:
                break
            print(f'ERRO! Não existe jogador com código {resposta}! Tente novamente.')
            resposta = int(input('Mostrar dados de qual jogador?: '))
            if resposta >= 0 and resposta < len(lista):
                break
    if resposta == 999:
        print('<< VOLTE SEMPRE >>')
        break
    contador = 0
    print(f'---LEVANTAMENTO DO JOGADOR {lista[resposta]["Nome"]}:')
    for dado in lista[resposta]["Gols"]:
        print(f'    No jogo {contador+1} fez {dado} gols.')
        contador += 1
    print('-' * 35)