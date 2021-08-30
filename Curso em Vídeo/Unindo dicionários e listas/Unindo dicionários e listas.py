dados = {}
lista = []
lmulheres = []
lacimadamedia = []
somaidade = 0
while True:
    nome = input('Nome: ')
    dados['Nome'] = nome
    sexo = input('Sexo (M/F): ')
    sexo = sexo.lower()
    if sexo != 'm' and sexo != 'f':
        while True:
            print('Digite um sexo válido.')
            sexo = input('Sexo (M/F): ')
            sexo = sexo.lower()
            if sexo == 'm' or sexo == 'f':
                break
    dados['Sexo'] = sexo
    idade = int(input('Idade: '))
    somaidade += idade
    dados['Idade'] = idade
    lista.append(dados.copy())
    if sexo == 'f':
        lmulheres.append(dados.copy())
    resposta = input('Quer continuar? [S/N]: ')
    resposta = resposta.lower()
    if resposta != 's' and resposta != 'n':
        while True:
            print('Digite uma resposta válida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta = resposta.lower()
            if resposta == 's' or resposta == 'n':
                break
    elif resposta == 's':
        None
    elif resposta == 'n':
        break
qntpessoas = len(lista)
for pessoa in lista:
    if pessoa['Idade'] > somaidade / len(lista):
        lacimadamedia.append(pessoa)
print('_'*60)
print(f' - Foram cadastradas no total {qntpessoas} pessoas')
print(f' - A média de idade do grupo é {somaidade/ len(lista)}')
print(f' - As mulheres cadastradas foram: ', end='')
if len(lmulheres) == 0:
    print(0)
else:
    for c in range(0, len(lmulheres)):
        if c == len(lmulheres)-1:
            print(f'{lmulheres[c]["Nome"]}')
        else:
            print(f'{lmulheres[c]["Nome"]}', end= ' - ')
print('-'*50)
print(' - Lista das pessoas que estão acima da média: ')
if len(lacimadamedia) == 0:
    print(0)
else:
    for c in range(0, len(lacimadamedia)):
        print(f'{c+1}ª pessoa: {lacimadamedia[c]["Nome"], lacimadamedia[c]["Sexo"], lacimadamedia[c]["Idade"]}')
    print('-'*50)




