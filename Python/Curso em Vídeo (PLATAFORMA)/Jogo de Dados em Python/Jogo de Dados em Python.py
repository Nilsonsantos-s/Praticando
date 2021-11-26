from random import randint
from operator import itemgetter
from time import sleep
dados = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1,6)}
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = []
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  ==  RANKING DOS JOGADORES ==')
for pos, v in enumerate(ranking):
    print('{}º lugar: {} com {}'.format(pos+1, v[0], v[1]))
    sleep(1)
