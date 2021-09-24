#Classe ---
class Bola:
    def __init__(self, nome, cor, circunferência=False, material=False):
        self.nome = nome
        self.cor = cor
        self.circunferência = circunferência
        self.material = material

    def mostraCor(self):
        print(f'A cor da bola "{self.nome}" é {self.cor}')

    def trocaCor(self, cor):
        self.cor = cor

#Funções ---
from time import sleep

def menu():
    while True:
        print('-' * 30)
        print(f'{"OPÇÕES":^28}')
        print('-' * 30)
        print('[1] Mostrar Cor')
        print('[2] Trocar Cor')
        print('[3] Parar Programa')
        opcao = int(input('OPÇÃO: '))
        if opcao == 1:
            try:
                b1.mostraCor()
            except:
                print('ERRO na hora de mostrar a cor!')
                sleep(1)
                menu()
            else:
                sleep(2)
        elif opcao == 2:
            novacor = input('Digite a nova cor: ')
            while novacor.isalpha() == False:
                print('Digite somente caracteres.')
                novacor = input('Digite a nova cor: ')
            try:
                b1.trocaCor(novacor)
            except:
                print('ERRO na hora de trocar de cor!')
                sleep(1)
                menu()
            else:
                print('Cor trocada com sucesso!')
                sleep(1.30)
        elif opcao == 3:
            print('------ Até logo! ------')
            break

def checarString(str):
    while str.isalpha() == False:
        str = input('Digite somente caracteres: ')

#Programa Principal ---
nome = input('Nome da bola: ')
checarString(nome)
cor = input('Cor: ')
checarString(cor)
while True:
    try:
        circun = int(input('Circunferência: '))
    except ValueError:
        print('Digite um número inteiro válido.')
    else:
        break
material = input('Material: ')
checarString(material)

b1 = Bola(nome, cor, circun, material)
menu()


