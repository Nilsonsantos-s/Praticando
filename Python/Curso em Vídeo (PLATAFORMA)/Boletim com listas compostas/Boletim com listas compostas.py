lista = [[], [[], []]]
while True:
    nome = input('Nome: ')
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    lista[0].append(nome)
    lista[1][0].append(n1)
    lista[1][1].append(n2)
    resposta = input('Deseja continuar? [S/N]: ')
    resposta.lower()
    if resposta == 'n':
        break
    if resposta != 'n' and resposta != 's':
        while resposta != 'n' and resposta != 's':
            print('Digite uma resposta válida.')
            resposta = input('Deseja continuar? [S/N]: ')
            resposta.lower()

media = []
for c in range(0, len(lista[1][0])):
    media.append((lista[1][0][c] + lista[1][1][c]) / 2)
print('-'*40)
print('No.      NOME              MÉDIA')
for pos, name in enumerate(lista[0]):
    print('{:^3} {:^15}{:^20}'.format(pos, name, round(media[pos], 1)))
print('-'*40)



