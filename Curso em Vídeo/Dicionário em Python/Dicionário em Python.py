nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))
if media > 6:
    resultado = 'aprovado'
else:
    resultado = 'reprovado'
dados = {'nome': nome, 'média': media, 'resultado': resultado}
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["média"]}')
print(f'Resultado é igual a {dados["resultado"]}')
