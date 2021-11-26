class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimirValores(self):
        print(f'X: {self.x}')
        print(f'Y: {self.y}')

class Retângulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        Xmeio = (A.x + B.x) / 2
        Ymeio = (A.y + B.y) / 2
        print(f'Xmeio = {Xmeio}')
        print(f'Ymeio = {Ymeio}')


def cor(string, azul=False, vermelho=False):
    if vermelho == True:
        print(f'\033[1;31m{string}\033[m')
    elif azul == True:
        print(f'\033[1;34m{string}\033[m')
    else:
        print(f'\033[1;36m{string}\033[m')

def menu():
    print('-' * 40)
    cor('[1]Alterar valores do retângulo', azul=True)
    cor('[2]Mostrar as coordenadas', azul=True)
    cor('[3]Calcular o centro do retângulo', azul=True)
    cor('[4]Sair do programa', azul=True)
    opção = int(input('Opção: '))
    if opção == 1:
        ax = int(input('Digite a coordenada x do canto inferior esquerdo: '))
        A.x = ax
        ay = int(input('Digite a coordenada y do canto inferior esquerdo: '))
        A.y = ay
        bx = int(input('Digite a coordenada x do canto superior direito: '))
        B.x = bx
        by = int(input('Digite a coordenada y do canto superior direito: '))
        B.y = by
        r1.largura = A
        r1.altura = B
        menu()
    elif opção == 2:
        print('Ponto inferior esquerdo')
        A.imprimirValores()
        print('Ponto superior direito')
        B.imprimirValores()
        continuar = input('Pressione Enter para continuar ')
        menu()
    elif opção == 3:
        r1.encontrarCentro()
        continuar = input('Pressione Enter para continuar ')
        menu()
    elif opção == 4:
        print('-'*40)
        cor('Até logo!')

##-----------------------------------------------------------------------
ax = int(input('Digite a coordenada x do canto inferior esquerdo: '))
ay = int(input('Digite a coordenada y do canto inferior esquerdo: '))
bx = int(input('Digite a coordenada x do canto superior direito: '))
by = int(input('Digite a coordenada y do canto superior direito: '))
A = Ponto(ax, ay)
B = Ponto(bx, by)
r1 = Retângulo(A, B)
menu()