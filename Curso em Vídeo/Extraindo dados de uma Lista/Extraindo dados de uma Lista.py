lista = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    resposta = input('Quer continuar? [S/N]: ')
    resposta = resposta.lower()
    if resposta != 'n' and resposta != 's':
        while resposta != 'n' and resposta != 's':
            print('Digite uma resposta válida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta = resposta.lower()
    if resposta == 'n':
        break
lista.sort(reverse=True)
print('A lista é: {}'.format(lista))
print('Foram digitados {} números.'.format(len(lista)))
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
