lista = [[], []]
tamanholista = []
resposta = 's'
while True:
    if resposta == 'n':
        break
    item = input('Digite um item: ')
    lista[0].append(item)
    lista[1].append(len(item))
    resposta = input('Quer continuar? [S/N]: ')
    resposta.lower()
    if resposta == 'n':
        break
    if resposta != 's' and resposta != 'n':
        while resposta != 's' and resposta != 'n':
            print('Digite uma resposta válida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta.lower()
lista[1] = sorted(lista[1])
copialista = []
for c in range(0, len(lista[1])):
    for elemento in lista[0]:
        tamanho = len(elemento)
        if tamanho == lista[1][c]:
            if elemento in copialista:
                None
            else:
                copialista.append(elemento)
print('-'*90)
print('A lista em ordem fica: ')
print(copialista)
print('-'*90)
