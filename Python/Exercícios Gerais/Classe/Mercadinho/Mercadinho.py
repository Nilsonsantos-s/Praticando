#Variável Global para testar se o carrinho está cheio.
global cheio
cheio = 'no'
#-------------------------------------------------------------

#Classes
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
        if len(self.produtos) == 5:
            global cheio
            cheio = 'yes'

    def lista_produto(self):
        if not self.produtos:
            print('Carrinho vazio.')
        else:
            print(f'{"PRODUTO":<12} VALOR')
            for produto in self.produtos:
                print(f'{produto.nome:<12} R${produto.valor:.2f}')

    def soma_total(self):
        if not self.produtos:
            print('Nada para somar.')
        else:
            total = 0
            for pos, produto in enumerate(self.produtos):
                if pos == len(self.produtos) - 1:
                    print(produto.nome, end=' == TOTAL: ')
                else:
                    print(produto.nome, end=' + ')
                total += produto.valor
            print(f'R${total:.2f}')

    @staticmethod
    def adicionar():
        print(dic)
        while True:
            escolha = input('Digite um produto: ')
            escolha = escolha.capitalize()
            if escolha in dic['nome']:
                if p1.nome == escolha:
                    carrinho.inserir_produto(p1)
                elif p2.nome == escolha:
                    carrinho.inserir_produto(p2)
                elif p3.nome == escolha:
                    carrinho.inserir_produto(p3)
                elif p4.nome == escolha:
                    carrinho.inserir_produto(p4)
                elif p5.nome == escolha:
                    carrinho.inserir_produto(p5)
                break
            else:
                print('\033[1;31mProduto indisponível.\033[m')
                print(dic)

    @staticmethod
    def menu():
        while True:
            print('\033[1;35m---MERCADO DA VIZINHA---\033[m')
            print('[1] Inserir produto')
            print('[2] Checar carrinho')
            print('[3] Somar produtos')
            print('[4] Sair do Programa')
            opção = input('Opção: ')
            if opção == '1':
                if cheio != 'yes':
                    CarrinhoDeCompras.adicionar()
                else:
                    print('Não é possível adicionar mais itens. Carrinho cheio!')
            elif opção == '2':
                carrinho.lista_produto()
            elif opção == '3':
                carrinho.soma_total()
            elif opção == '4':
                print('Até logo!')
                break
            else:
                print('Digite uma opção válida.')

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
#-------------------------------------------------------------

#Programa Principal-------
carrinho = CarrinhoDeCompras()
p1 = Produto('Iphone', 4000.00)
p2 = Produto('Camiseta', 20.00)
p3 = Produto('Caneca', 4.00)
p4 = Produto('Sabonete', 3.00)
p5 = Produto('Chocolate', 1.00)
dic = {'nome': [p1.nome, p2.nome, p3.nome, p4.nome, p5.nome], 'valor': [p1.valor,
    p2.valor, p3.valor, p4.valor, p5.valor]}
CarrinhoDeCompras.menu()