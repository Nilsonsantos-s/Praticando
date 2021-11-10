class Funcionário:
    def __init__(self, nome, salário):
        self.nome = nome
        self.salário = float(salário)

    def imprimirNome(self):
        return print(f'Nome do Funcionário: {self.nome}')

    def imprimirSalário(self):
        return print(f'Salário: R${self.salário:.2f}')

import gc
métodos = list()

nome = input('Digite um nome: ')
salário = float(input('Digite um salário: '))
f = Funcionário(nome, salário)
print('-'*70)
print(f'Classe: {Funcionário}')
for c in dir(Funcionário):
    if c[0] != '_':
        métodos.append(c)
print(f'Métodos: {", ".join(métodos)}')
print('Objetos: ', end='')
for obj in gc.get_objects():
    if isinstance(obj, Funcionário):
        print(f'  ---  {obj}', end= '')
print()
print('-'*70)
f.imprimirNome()
f.imprimirSalário()


