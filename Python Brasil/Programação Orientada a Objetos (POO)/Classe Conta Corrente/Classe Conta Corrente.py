from time import sleep
##Classe ---
class Conta_Corrente:
    def __init__(self, contaid, nome, saldo):
        self.contaid = contaid
        self.nome = nome
        self.saldo = saldo

    def AlterarNome(self):
        nome = input('Novo Nome: ')
        while nome.isalpha() == False:
            nome = input('Digite somente letras: ')
        try:
            self.nome = nome
        except:
            print('ERRO! Não foi possível alterar o nome!')
        else:
            print('Nome alterado com sucesso!')
        finally:
            sleep(1)
            self.exibirMenu()

    def Depositar(self):
        try:
            while True:
                try:
                    valor = float(input('Valor do Depósito: R$'))
                except ValueError:
                    print('ERRO! Tipo inválido.')
                else:
                    self.saldo += valor
                    break
        except:
            print('ERRO! Não foi possível realizar o depósito!')
        else:
            print(f'R${valor:.2f} depositado com sucesso!')
        finally:
            sleep(1)
            self.exibirMenu()

    def Sacar(self):
        try:
            while True:
                try:
                    while True:
                        valor = float(input('Valor do Saque: '))
                        if valor > self.saldo:
                            print('Valor máximo ultrapassado! Tente novamente.')
                        else:
                            self.saldo -= valor
                            break
                except ValueError:
                    print('ERRO! Tipo inválido.')
                else:
                    break
        except:
            print('ERRO! Não foi possível realizar o saque!')
        else:
            print(f'R${valor:.2f} sacado com sucesso!')
        finally:
            sleep(1)
            self.exibirMenu()

    def exibirMenu(self):
        print('-' * 40)
        print(f'{"CONTA CORRENTE":^38}')
        print('-' * 40)
        print(f'Nome: {self.nome}')
        print(f'ID: {self.contaid}')
        print(f'Saldo: {self.saldo:.2f}')
        print('-' * 40)
        print('[1] Alterar Nome')
        print('[2] Depositar')
        print('[3] Saque')
        print('[4] Encerrar')
        print('-' * 40)
        while True:
            try:
                while True:
                    opcao = int(input('Opção: '))
                    if opcao < 1 or opcao > 4:
                        print('Opção inválida!')
                    else:
                        break
            except ValueError:
                print('Opção inválida!')
            else:
                break
        if opcao == 1:
            self.AlterarNome()
        elif opcao == 2:
            self.Depositar()
        elif opcao == 3:
            self.Sacar()
        elif opcao == 4:
            print('---- Até logo! ----')


##Programa Principal ---
nome = input('Nome: ')
while nome.isalpha() == False:
    nome = input('Digite somente letras: ')
while True:
    try:
        contaid = int(input('Número da Conta: '))
    except ValueError:
        print('ERRO! Tipo inválido.')
    else:
        break
while True:
    try:
        saldo = float(input('Saldo: R$'))
    except ValueError:
        print('ERRO! Tipo inválido.')
    else:
        break

c1 = Conta_Corrente(contaid, nome, saldo)
c1.exibirMenu()


