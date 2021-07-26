import random
numero = random.randint(0,5)
print('=====JOGO DA ADIVINHAÇÃO=====')
print('Sorteamos um número de 0 a 5!\nAdivinhe qual foi esse número!')
n1 = int(input('Digite aqui o número: '))
if numero == n1:
    print('Parabéns, você é o vencedor!')
else:
    print('Você perdeu, o número foi {}!'.format(numero))
