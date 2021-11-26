maioridade = int()
menoridade = int()
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?: '.format(c)))
    if 2021-ano >= 18:
        maioridade = maioridade + 1
    elif 2021-ano < 18:
        menoridade = menoridade + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maioridade))
print('E também tivemos {} pessoas menores de idade'.format(menoridade))