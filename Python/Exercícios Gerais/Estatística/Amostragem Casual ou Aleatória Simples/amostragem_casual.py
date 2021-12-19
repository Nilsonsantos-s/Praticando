import random
print('-'*40)
print('AMOSTRAGEM CASUAL OU ALEATÓRIA SIMPLES')
populacao = [numero for numero in range(1, 31)]
print('População:', populacao)
print('Amostra:', random.choices(populacao, k=8))
