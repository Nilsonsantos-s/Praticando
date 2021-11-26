##Classe---
class Retângulo:
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB

    @classmethod
    def MudarValorDosLados(cls, A, B):
        return cls(A, B)

    def RetornarValores(self):
        try:
            print(f'Comprimento: {self.LadoA} \nLargura: {self.LadoB}')
        except:
            print('ERRO! Problema na hora de retornar os valores!')
        finally:
            sleep(1)
            menu()

    @classmethod
    def CalcularÁrea(cls, A, B):
        print(f'ÁREA: {A*B}m²')

    @classmethod
    def CalcularPerímetro(cls, A, B):
        print(f'PERÍMETRO: {A+B}')



##Funções---
from time import sleep
def menu():
    print('[1] Mudar valores')
    print('[2] Retornar valores')
    print('[3] Calcular área')
    print('[4] Calcular perímetro')
    print('[5] Sair do programa e Calcular Quantidade de Pisos')
    escolha = int(input('Digite uma opção: '))
    if escolha == 1:
        while True:
            try:
                loca = int(input('Comprimento: '))
            except ValueError:
                print('ERRO! Tipo inválido!')
            else:
                break
        while True:
            try:
                locb = int(input('Largura: '))
            except ValueError:
                print('ERRO! Tipo inválido!')
            else:
                break
        global r1
        try:
            r1 = Retângulo.MudarValorDosLados(loca, locb)
        except:
            print('ERRO! Problema na hora de mudar os valores!')
        else:
            print('Valores alterados com sucesso!')
        finally:
            sleep(1)
            menu()
    elif escolha == 2:
        r1.RetornarValores()
    elif escolha == 3:
        try:
            Retângulo.CalcularÁrea(r1.LadoA, r1.LadoB)
        except:
            print('ERRO! Problema na hora de calcular a área!')
        finally:
            sleep(1)
            menu()
    elif escolha == 4:
        try:
            Retângulo.CalcularPerímetro(r1.LadoA, r1.LadoB)
        except:
            print('ERRO! Problema na hora de calcular o perímetro!')
        finally:
            sleep(1)
            menu()
    elif escolha == 5:
        print('-'*40)
        print(f'Comprimento: {r1.LadoA}m \nLargura: {r1.LadoB}m')
        print(f'Área: {r1.LadoA * r1.LadoB}m²')
        print(f'Metragem do Piso: {mpiso}m²')
        print(f'Quantidade de Pisos necessários: {float((r1.LadoA * r1.LadoB) / mpiso):.0f}')
        print('-' * 40)

        print('---- Até logo! ----')
    else:
        print('Digite uma opção válida!')
        sleep(1)
        menu()


##Programa Principal---
mpiso = 0.2025
print(f'Metragem do Piso: {mpiso}m²')
print('-'*40)
print('Informe as medidas de um local.')
while True:
    try:
        la = int(input('Digite o comprimento (m): '))
    except ValueError:
        print('ERRO! Tipo inválido!')
    else:
        break
while True:
    try:
        lb = int(input('Digite a largura (m): '))
    except ValueError:
        print('ERRO! Tipo inválido!')
    else:
        break
print('-'*40)
r1 = Retângulo(la, lb)
menu()






