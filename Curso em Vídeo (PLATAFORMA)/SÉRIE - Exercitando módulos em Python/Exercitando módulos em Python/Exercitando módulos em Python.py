from módulos import moeda
p = float(input('Digite um preço: '))
print(f'A metade de {p} é igual a {moeda.metade(p)}')
print(f'O dobro de {p} é igual a {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
