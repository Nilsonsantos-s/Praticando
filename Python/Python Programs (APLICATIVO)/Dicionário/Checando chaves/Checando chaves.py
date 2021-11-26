from random import randint
dados = {}
for c in range(1, 6):
    num = randint(1, 9)
    num2 = randint(1, 9)
    dados[num] = num2
print('Verifique a existência da chave')
resposta = int(input(('Digite um número de 1 a 9: ')))
if resposta > 9 or resposta < 1:
    while resposta > 9 or resposta < 1:
        print('Dado inválido.', end=' ')
        resposta = int(input(('Digite um número de 1 a 9: ')))
print('=' * 47)
if resposta in dados.keys():
    print(f'A chave {resposta} existe no dicionário e seu valor é {dados[resposta]}.')
else:
    print(f'A chave {resposta} não está no dicionário.')
print('=' * 47)
print(dados.keys())
print(dados.items())
