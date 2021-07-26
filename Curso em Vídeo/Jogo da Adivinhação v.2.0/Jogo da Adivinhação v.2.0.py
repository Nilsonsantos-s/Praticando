import random
import os
resposta = 's'
computador = 0
num = 1
palpite = int()
computador = random.randint(1,10)
while resposta == 's' and computador != num:
    num = int(input('Digite um número entre 0 e 10: '))
    palpite = palpite + 1
    if  computador != num:
        if num < computador:
            resposta = input('Mais... Deseja tentar novamente? [S/N]: ')
            resposta = resposta.lower()
        elif num > computador:
            resposta = input('Menos... Deseja tentar novamente? [S/N]: ')
            resposta = resposta.lower()
        elif resposta == 'n':
            print('Ok! :) Volte sempre!')
    elif computador == num:
        print('VITÓRIA!!! ')
        print('Foram necessários {} palpites para vencer.'.format(palpite))
        resposta = resposta.lower()



