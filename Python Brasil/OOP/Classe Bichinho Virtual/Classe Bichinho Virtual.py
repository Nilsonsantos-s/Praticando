class Bichinho:
    @classmethod
    def exibirHumor(cls, fome, saúde):
        if fome <= 15 and saúde >= 50:
            print('\033[1;36mNormal\033[m')
        elif fome >= 15 and saúde >= 50:
            print('\033[1;32mFeliz\033[m')
        elif fome <= 15 and saúde < 50:
            print('\033[1;31mTriste\033[m')

    def __init__(self, nome, fome, saúde, idade):
        self.nome = nome
        self.fome = fome
        self.saúde = saúde
        self.idade = idade

    def alterarAtributos(self):
        self.nome = input('Nome: ')
        while True:
            try:
                self.fome = int(input('Fome: '))
            except ValueError:
                print('\033[1;31mTipo inválido! Tente novamente.\033[m')
            else:
                break
        while True:
            try:
                self.saúde = int(input('Saúde: '))
            except ValueError:
                print('\033[1;31mTipo inválido! Tente novamente.\033[m')
            else:
                break
        while True:
            try:
                self.idade = int(input('Idade: '))
            except ValueError:
                print('\033[1;31mTipo inválido! Tente novamente.\033[m')
            else:
                break

    def retornarAtributos(self):
        print('-' * 40)
        print(f'{"NOME":10}{"FOME":10}{"SAÚDE":10}{"IDADE"}')
        print(f'{self.nome:10}{self.fome:<10}{self.saúde:<10}{self.idade}')
        print('-' * 40)

    def menu(self):
        print('[1] Alterar Atributos')
        print('[2] Retornar Atributos')
        print('[3] Sair')
        try:
            opção = int(input('Opção: '))
        except ValueError:
            print('\033[1;31mTipo inválido! Tente novamente.\033[m')
        else:
            if opção == 1:
                try:
                    self.alterarAtributos()
                except:
                    print('Ocorreu um erro na hora de alterar os atributos.')
            elif opção == 2:
                try:
                    self.retornarAtributos()
                    Bichinho.exibirHumor(self.fome, self.saúde)
                except:
                    print('Ocorreu um erro na hora de retornar os atributos.')
            elif opção == 3:
                print('Até mais!')

            else:
                print('\033[1;31mDigite uma opção válida!\033[m')
        finally:
            if opção == 3:
                None
            else:
                self.menu()


nome = input('Nome: ')
b1 = Bichinho(nome=nome, fome=30, saúde=50, idade=0)
b1.menu()





