class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.gasolina = None

    def adicionarGasolina(self, gasolina):
        gasolina = int(gasolina)
        self.gasolina = gasolina

    def obterGasolina(self):
        return print(self.gasolina)

    def Andar(self, km):
        print(f'Você dirigiu por {km} quilômetros')
        litrousado = km/self.consumo
        print(f'Utilizou {litrousado:.2f} litros de gasolina.')
        self.gasolina -= litrousado

    def menu(self):
        while True:
            print('[1] Abastecer')
            print('[2] Mostrar gasolina')
            print('[3] Dirigir')
            print('[4] Sair do programa')
            opção = input('Opção: ')
            if opção == '1':
                while True:
                    quantia = input('Digite a quantidade: ')
                    if not quantia.isnumeric():
                        print('Digite apenas números inteiros.')
                    else:
                        c1.adicionarGasolina(quantia)
                        break
            elif opção == '2':
                if self.gasolina == None:
                    print('Não há gasolina disponível.')
                else:
                    c1.obterGasolina()
            elif opção == '3':
                if self.gasolina == None or self.gasolina == 0.00:
                    print('Não há gasolina para dirigir. Adicione primeiro.')
                else:
                    while True:
                        km = input('Deseja dirigir por quantos quilômetros?: ')
                        if not km.isnumeric():
                            print('Digite apenas números inteiros.')
                        else:
                            km = int(km)
                            if self.gasolina < km/self.consumo:
                                print('A distância é muito longa. Precisa-se de mais gasolina!')
                                while True:
                                    resposta = input('Deseja retornar ao Menu Principal? [S/N]: ')
                                    resposta = resposta.lower()
                                    if resposta == 's':
                                        break
                                    elif resposta == 'n':
                                        break
                                    else:
                                        print('Opção inválida.')
                                if resposta == 's':
                                    break
                            else:
                                c1.Andar(km)
                                break
            elif opção == '4':
                print('Até mais!')
                break
            else:
                print('Opção inválida.')


c1 = Carro(10)
c1.menu()



