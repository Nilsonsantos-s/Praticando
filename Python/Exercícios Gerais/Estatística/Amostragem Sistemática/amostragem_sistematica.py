import random
pecas = [peca for peca in range(1, 101)]
intervalo = int(len(pecas) / 20)
numero_inicial = random.randint(1, intervalo)
amostra = []
for peca in pecas:
    if peca % numero_inicial == 0:
        amostra.append(peca)
    if len(amostra) == 20:
        break
print('-'*30+'Amostragem Sistemática'+'-'*30)
print('Peças:', pecas)
print('Amostra adquirida sistematicamente:', amostra)



