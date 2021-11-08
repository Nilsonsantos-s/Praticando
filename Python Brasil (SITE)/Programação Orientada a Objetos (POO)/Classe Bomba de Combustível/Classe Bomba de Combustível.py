class bombaCombustível():
    lista = ['Álcool', 'Diesel']
    def __init__(self, tipoCombustível, valorLitro, quantidadeCombustível):
        self.tipoCombustível = tipoCombustível
        self.valorLitro = valorLitro
        self.quantidadeCombustível = quantidadeCombustível
        self.dados = {'tipoCombustível': ['Álcool', 'Diesel'], 'Valor': [4.50, 5]
            , 'Quantidade': [1000, 1000]}

    def abastecerPorValor(self, preço):
        quantidade = preço // self.valorLitro
        self.alterarQuantidadeCombustível(quantidade)
        print(f'Você gastou R${preço:.2f}')
        print(f'A quantidade de litros ganhos é {quantidade:.0f}')
        voltar = input('Pressione Enter para retornar ao Menu Principal ')

    def abastecerPorLitro(self, litro):
        preço = litro * self.valorLitro
        self.alterarQuantidadeCombustível(litro)
        print(f'Você gastou R${preço:.2f}')
        print(f'A quantidade de litros ganhos é {litro:.0f}')
        voltar = input('Pressione Enter para retornar ao Menu Principal ')

    def alterarQuantidadeCombustível(self, quantidade):
        self.quantidadeCombustível -= quantidade
        if self.tipoCombustível == 'Álcool':
            self.dados['Quantidade'][0] -= quantidade
        elif self.tipoCombustível == 'Diesel':
            self.dados['Quantidade'][1] -= quantidade

    def alterarValor(self, valor):
        self.valorLitro = valor
        if self.tipoCombustível == 'Diesel':
            self.dados['Valor'][1] = valor
        elif self.tipoCombustível == 'Álcool':
            self.dados['Valor'][0] = valor

    def alterarCombustível(self):
        print(bombaCombustível.lista)
        combustível = input('Escolha um combustível: ')
        while combustível not in bombaCombustível.lista:
            print(f'{combustível} não existe na lista.')
            combustível = input('Escolha um combustível: ')
        self.tipoCombustível = combustível


    def menu(self):
        while True:
            contador = 0
            print('-' * 50)
            for key, values in self.dados.items():
                contador += 1
                if contador == 1:
                    print(f'{key:15} - {self.tipoCombustível}')
                else:
                    if self.tipoCombustível == 'Diesel':
                        print(f'{key:15} - {values[1]}')
                    elif self.tipoCombustível == 'Álcool':
                        print(f'{key:15} - {values[0]}')
            print('-' * 50)
            print('[1] Abastecer por valor')
            print('[2] Abastecer por litro')
            print('[3] Alterar combustível')
            print('[4] Encerrar programa')
            opção = input('Opção: ')
            if opção == '1':
                while True:
                    try:
                        valor = float(input('Digite um valor: R$'))
                    except ValueError:
                        print('Valor inválido.')
                    else:
                        qnt = valor // self.valorLitro
                        if qnt > self.quantidadeCombustível:
                            print('Limite excedido. Tente novamente.')
                        else:
                            b1.abastecerPorValor(valor)
                            break
            elif opção == '2':
                while True:
                    try:
                        quantidade = int(input('Digite a quantidade: '))
                    except ValueError:
                        print('Valor inválido.')
                    else:
                        if quantidade > self.quantidadeCombustível:
                            print('Limite excedido. Tente novamente.')
                        else:
                            b1.abastecerPorLitro(quantidade)
                            break
            elif opção == '3':
                b1.alterarCombustível()
            elif opção == '4':
                print('Até logo!')
                break
            else:
                print('Opção inválida!')
                sleep(1)

from time import sleep
b1 = bombaCombustível('Álcool', 4.50, 1000)
b1.menu()
