#Classes---
class Quadrado:
    def __init__(self, nome, tamanholado):
        self.tamanholado = tamanholado
        self.nome = nome

    def mudarvalorLado(self, tamanho):
        self.tamanholado = tamanho

    def retornarvalorLado(self):
        print(f'Tamanho: {self.tamanholado}')

    def calcularArea(self):
        print(f'Área: {self.tamanholado*2}')

#Funções---
def menu(square):
    print('-'*30)
    print(f'QUADRADO {square.nome}')
    print('-' * 30)
    print('[1] Retornar valor dos lados')
    print('[2] Mudar valor dos lados')
    print('[3] Calcular área')
    print('[4] Sair do Programa')
    print('-' * 30)
    opcao = int(input('Opção: '))
    while True:
        if opcao == 1:
            try:
                square.retornarvalorLado()
            except:
                print('ERRO! Ocorreu um problema ao retornar o valor do lado!')
            finally:
                menu(square)
        elif opcao == 2:
            while True:
                try:
                    valor = int(input('Digite o tamanho: '))
                except ValueError:
                    print('ERRO! Digite um número inteiro válido.')
                else:
                    print('Tamanho alterado com sucesso!')
                    break
            square.mudarvalorLado(valor)
            menu(square)
        elif opcao == 3:
            try:
                square.calcularArea()
            except:
                print('ERRO! Ocorreu um problema ao calcular a área!')
            finally:
                menu(square)
        elif opcao == 4:
            print('----- Até logo! -----')
            break
        else:
            opcao = int(input(('ERRO! Digite uma opção válida: ')))

#Programa Principal---
nomeq = input('Digite o nome do quadrado: ')
while nomeq.isalpha() == False:
    print('ERRO! Digite um nome com caracteres. ')
    nomeq = input('Digite o nome do quadrado: ')
while True:
    try:
        tamanhoq = int(input('Digite o tamanho dos lados: '))
    except ValueError:
        print('ERRO! Digite um número inteiro válido. ')
    else:
        break
g1 = Quadrado(nomeq, tamanhoq)
menu(g1)



