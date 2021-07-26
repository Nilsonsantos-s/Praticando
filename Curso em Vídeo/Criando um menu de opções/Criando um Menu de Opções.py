n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
resposta = int()
while resposta != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    resposta = int(input('Opção: '))
    if resposta == 1:
        print('{}+{} = {}'.format(n1, n2, n1+n2))
    elif resposta == 2:
        print('{}*{} = {}'.format(n1, n2, n1*n2))
    elif resposta == 3:
        if n1 > n2:
            print('O número maior é {}'.format(n1))
        elif n2 > n1:
            print('O número maior é {}'.format(n2))
        elif n1 == n2:
            print('Os números são iguais.')
    elif resposta == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo: '))
    elif resposta == 5:
        print('Ok! :) Volte sempre!')
    elif resposta > 5 or resposta < 1:
        print('Opção inválida. Tente novamente.')
