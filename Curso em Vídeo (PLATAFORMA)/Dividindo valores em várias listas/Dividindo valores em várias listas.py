lista = []
listapar = []
listaímpar = []
while True:
    numero = int(input('Digite um número: '))
    resposta = input('Quer continuar? [S/N]: ')
    resposta = resposta.lower()
    lista.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaímpar.append(numero)
    if resposta != 's' and resposta != 'n':
        while resposta != 's' and resposta != 'n':
            print('Digite uma resposta válida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta = resposta.lower()
    if resposta == 'n':
        break
print('='*30)
print('Lista de números:', lista)
print('Números pares:', listapar)
print('Números ímpares:', listaímpar)
print('='*30)

