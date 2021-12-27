import random

populacao = [numero for numero in range(1, 101)]
for pos, numero in enumerate(populacao):
    populacao[pos] = random.randint(12, 80)
media = round(sum(populacao) / len(populacao))
print(f'Idades:\n{populacao}')
print('Média de Idade:', media)