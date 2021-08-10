lista = []
while True:
    numero = int(input('Digite o valor: '))
    if numero in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(numero)
    resposta = input('Quer continuar? [S/N]: ')
    resposta = resposta.lower()
    if resposta != 's' and resposta != 'n':
        while True:
            print('Digite uma resposta válida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta = resposta.lower()
            if resposta == 's' or resposta == 'n':
                break
    if resposta == 'n':
        break
print('Você digitou os valores:', sorted(lista))
