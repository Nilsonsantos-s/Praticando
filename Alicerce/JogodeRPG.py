import time
import os
import random
nome = input('Olá, por favor, digite seu nome: ')
print('Você acorda no meio da floresta')
time.sleep(2)
print('Uma grande caverna está ao seu lado')
time.sleep(2)
print('Você não sabe o porquê mas algo te impulsiona a entrar na caverna')
time.sleep(3)
HP = int(100)
MP = int(100)
HPm1 = int(100)
MPm1 = int(100)
level = int(1)
exp = int(0)
vitoria = int()
derrota = int()
ganharlevel = int(60)
os.system('cls')
print('Você encontra um monstro!')
contadorb1 = int(2)
while HP > 0 and HPm1 > 0:
    time.sleep(1)
    print('\n' * 100)
    print('HP: {}  -----   MP: {}     |     MonstroHP: {} ---- MonstroMP: {}'.format(HP, MP, HPm1, MPm1))
    if contadorb1 % 2 == 0:
        opcao1 = int(input('[1] Atacar monstro   [2] Dar martelada: '))
        if opcao1 == 1:
            print('Você ataca o monstro!')
            HPm1 = HPm1 - 15
        elif opcao1 == 2:
            if opcao1 == 2 and MP < 30:
                print('Sem MP!')
                contadorb1 = contadorb1 - 1
            else:
                print('Martelada!')
                HPm1 = HPm1 - 25
                MP = MP - 30
    else:
        chanceataquem1 = random.randint(0,10)
        if chanceataquem1 > 6:
            print('O monstro te dá SUPER GOLPEADA!')
            HP = HP - 25
        else:
            print('O monstro te ataca!')
            HP = HP - 15
    contadorb1 += 1
    if HPm1 <= 0:
        vitoria += 1
        exp += 30
        print('MONSTRO DERROTADO!')
        print('Você recebeu {} de experiência!'.format(exp))
        ganharlevel = ganharlevel - 30
        if ganharlevel == 0:
            level += 1
            print('Parabéns! Você passou para o nível {}!'.format(level))
        elif ganharlevel > 0:         
            print('Falta {} xp para passar de nível!'.format(ganharlevel))
    if HP <= 0:
        derrota += 1
        print('VOCÊ FOI DERROTADO!')
