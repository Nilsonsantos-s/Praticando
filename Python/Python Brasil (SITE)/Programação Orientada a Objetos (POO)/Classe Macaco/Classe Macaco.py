from time import sleep
class Macaco:
    global lista
    lista = ['hambúrguer', 'morango', 'macarrão', 'feijoada', 'maçã', 'macaco', 'banana']

    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho


    def exibirBucho(self):
        print(Macaco.cor('-'*30))
        print(f'Nome: {self.nome}')
        if not self.bucho:
            print(f'Bucho: vazio')
        else:
            print(f'Bucho: {self.bucho}')
        print(Macaco.cor('-' * 30))
        voltar = input('Pressione Enter para voltar ao Menu. ')

    def comer(self):
        while True:
            print(f'\033[1;32m{lista}\033[m')
            lanche = input(Macaco.cor('Digite um lanche: '))
            if lanche not in lista:
                print('\033[1;31mO lanche não está na lista\033[m')
            else:
                if lanche == 'macaco':
                    global gatilho
                    global ripmacaco
                    gatilho = 1
                    print(f'{self.nome} pratica atos de canibalismo', end='')
                    for c in range(1, 4):
                        print('.', end='')
                        sleep(1)
                    print()
                    if self.nome == m1.nome:
                        print(f'R.I.P {m2.nome}')
                        ripmacaco = m2.nome
                    elif self.nome == m2.nome:
                        print(f'R.I.P {m1.nome}')
                        ripmacaco = m1.nome
                    sleep(1)
                self.bucho.append(lanche)
                lista.remove(lanche)
                print(Macaco.cor(f'{self.nome} foi alimentado(a) com sucesso!'))
                sleep(1)
                resposta = input(Macaco.cor('Deseja incluir mais um alimento? [S/N]: '))
                resposta = resposta.lower()
                if resposta == 's' and len(self.bucho) == 3:
                    print(Macaco.cor(f'O bucho de {self.nome} já está cheio. \nVoltando ao menu principal...', True))
                    sleep(3)
                    break
                if resposta == 'n':
                    break

    def digerir(self):
        try:
           self.bucho.clear()
        except:
            print(Macaco.cor('Ocorreu um erro na hora de digerir.', True))
        else:
            print(Macaco.cor('Digerido com sucesso!'))
            sleep(1)

    @staticmethod
    def cor(string, red=False):
        if red == False:
            novo = (f'\033[1;30m{string}\033[m')
            return novo
        else:
            novo = (f'\033[1;31m{string}\033[m')
            return novo

    @staticmethod
    def menu():
        while True:
            print('-' * 30)
            if gatilho == 1:
                if ripmacaco != m1.nome:
                    print(f'Macacos: \033[1;32m{m1.nome}\033[m')
                elif ripmacaco != m2.nome:
                    print(f'Macacos: \033[1;32m{m2.nome}\033[m')
            else:
                print(f'Macacos: \033[1;32m{m1.nome}\033[m --- \033[1;32m{m2.nome}\033[m')
            print(Macaco.cor('[1] Exibir bucho'))
            print(Macaco.cor('[2] Alimentar macaco'))
            print(Macaco.cor('[3] Digerir lanche'))
            print(Macaco.cor('[4] Encerrar o programa'))
            print('-' * 30)
            try:
                opcao = int(input('Opção: '))
            except ValueError:
                print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                sleep(0.50)
            else:
                if opcao == 1:
                    if gatilho == 1:
                        if ripmacaco == m1.nome:
                            m2.exibirBucho()
                        else:
                            m1.exibirBucho()
                    else:
                        while True:
                            print(Macaco.cor('Selecione um macaco: '))
                            print(f'[1] {m1.nome}')
                            print(f'[2] {m2.nome}')
                            try:
                                opcao = int(input(''))
                            except ValueError:
                                print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                                sleep(0.50)
                            else:
                                if opcao == 1:
                                    m1.exibirBucho()
                                    break
                                elif opcao == 2:
                                    m2.exibirBucho()
                                    break
                                else:
                                    print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                                    sleep(0.50)
                elif opcao == 2:
                    if gatilho == 1:
                        if ripmacaco == m1.nome:
                            if len(m2.bucho) == 3:
                                print(Macaco.cor(f'O bucho de {m2.nome} está cheio! Digira os lanches primeiro.'))
                                sleep(1)
                            else:
                                m2.comer()
                        if ripmacaco == m2.nome:
                            if len(m1.bucho) == 3:
                                print(Macaco.cor(f'O bucho de {m1.nome} está cheio! Digira os lanches primeiro.'))
                                sleep(1)
                            else:
                                m1.comer()
                    else:
                        if len(m1.bucho) == 3 and len(m2.bucho) == 3:
                            print(Macaco.cor('Os buchos estão cheios! Digira os lanches primeiro.'))
                            sleep(1)
                        else:
                            while True:
                                print(Macaco.cor('Selecione um macaco: '))
                                print(f'[1] {m1.nome}')
                                print(f'[2] {m2.nome}')
                                try:
                                    opcao = int(input(''))
                                except ValueError:
                                    print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                                    sleep(0.50)
                                else:
                                    if opcao == 1:
                                        if len(m1.bucho) == 3:
                                            print(Macaco.cor(f'O bucho de {m1.nome} está cheio.'))
                                        else:
                                            m1.comer()
                                        break
                                    elif opcao == 2:
                                        if len(m2.bucho) == 3:
                                            print(Macaco.cor(f'O bucho de {m2.nome} está cheio.'))
                                        else:
                                            m2.comer()
                                        break
                                    else:
                                        print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                                        sleep(0.50)
                elif opcao == 3:
                    if gatilho == 1:
                        if ripmacaco == m1.nome:
                            if not m2.bucho:
                                print(Macaco.cor(f'O bucho de {m2.nome} está vazio...', True))
                                sleep(2)
                            else:
                                m2.digerir()
                        elif ripmacaco == m2.nome:
                            if not m1.bucho:
                                print(Macaco.cor(f'O bucho de {m1.nome} está vazio...', True))
                                sleep(1)
                            else:
                                m1.digerir()
                    else:
                        if not m1.bucho and not m2.bucho:
                            print(Macaco.cor('Não há nada para ser digerido. Alimente-os primeiro.', True))
                            sleep(2)
                        else:
                            while True:
                                print(Macaco.cor('Selecione um macaco: '))
                                print(f'[1] {m1.nome}')
                                print(f'[2] {m2.nome}')
                                try:
                                    opcao = int(input(''))
                                except ValueError:
                                    print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                                    sleep(0.50)
                                else:
                                    if opcao == 1:
                                        if not m1.bucho:
                                            print(Macaco.cor(f'O bucho de {m1.nome} está vazio...', True))
                                            sleep(1)
                                        else:
                                            m1.digerir()
                                            break
                                    elif opcao == 2:
                                        if not m2.bucho:
                                            print(Macaco.cor(f'O bucho de {m2.nome} está vazio...', True))
                                        else:
                                            m2.digerir()
                                            break
                                    else:
                                        print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                                        sleep(0.50)
                elif opcao == 4:
                    print(Macaco.cor('Até logo!'))
                    break
                else:
                    print('\033[1;31mOpção inválida! Tente novamente.\033[m')
                    sleep(0.50)

##PROGRAMA PRINCIPAL
global gatilho
gatilho = 0
global ripmacaco
ripmacaco = ''
nome = input(Macaco.cor('Digite o nome do primeiro macaco: '))
while True:
    if len(nome) < 3:
        nome = input('\033[1;32mDigite um nome com no mínimo 3 letras:\033[m ')
    else:
        m1 = Macaco(nome, bucho=list())
        break
nome = input(Macaco.cor('Digite o nome do segundo macaco: '))
while True:
    if len(nome) < 3:
        nome = input('Digite um nome com no mínimo 3 letras: ')
    else:
        m2 = Macaco(nome, bucho=list())
        break
Macaco.menu()




