chave = input('Digite a chave: ')
valor = input('Digite o valor: ')
if valor.isnumeric() == True:
    valor = int(valor)
dados = {chave: valor}
print('='*22)
for k, v in dados.items():
    print(f'A chave é: {k}\nO valor da chave é: {v}')
print('='*22)
