##Classe
class TV:
    def __init__(self, volume, canal):
        self.volume = volume
        self.canal = canal

    def AumentarVolume(self):
        if self.volume == 50:
            print('Limite máximo atingido.')
        else:
            self.volume += 1

    def DiminuirVolume(self):
        if self.volume == 0:
            print('Limite mínimo atingido.')
        else:
            self.volume -= 1

    def MudardeCanal(self):
        while True:
            canal = int(input('Digite um canal: '))
            if canal > 50:
                print('O limite máximo é 50.')
            elif canal < 1:
                print('O limite mínimo é 1.')
            else:
                break
        self.canal = canal
##Funções
from time import sleep
def menu():
    print('------------------------')
    print(f'{"Volume":<7} - {tv1.volume:^4}')
    print(f'{"Canal":<7} - {tv1.canal:^4}')
    print('------------------------')
    print('[1] Aumentar Volume')
    print('[2] Diminuir Volume')
    print('[3] Mudar de Canal')
    print('------------------------')
    try:
        opçao = int(input('Digite uma opção: '))
    except ValueError:
        print('Tipo inválido! Tente novamente.')
    else:
        if opçao == 1:
            try:
                TV.AumentarVolume(tv1)
            except:
                print('Houve um erro!')
        elif opçao == 2:
            try:
                TV.DiminuirVolume(tv1)
            except:
                print('Houve um erro!')
        elif opçao == 3:
            try:
                TV.MudardeCanal(tv1)
            except:
                print('Houve um erro!')
        elif opçao > 3 or opçao < 1:
            print('Opção inválida. Tente novamente.')
    finally:
        menu()

while True:
    try:
        c = int(input('Informe o canal: '))
    except ValueError:
        print('Tipo inválido! Tente novamente.')
    else:
        if c > 50:
            print('O limite máximo é 50.')
        elif c < 1:
            print('O limite mínimo é 1.')
        else:
            break
tv1 = TV(volume=25, canal=c)
menu()




