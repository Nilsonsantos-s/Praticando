class Animal:
    listaanimal = ['Mamífero', 'Réptil', 'Peixe', 'Ave']
    animaiscriados = {1: [], 2: [], 3: [], 4: []}
    global vertrue
    vertrue = 'não'
    global contador
    contador = 0

    def __init__(self, peso, idade, membros):
        self.peso = peso
        self.idade = idade
        self.membros = membros

    @classmethod
    def checarAnimal(cls, animal, teste1=False, teste2= False):
        if teste1 == True:
            if animal == 'Mamífero':
                Mamífero.criarMamífero()
            elif animal == 'Réptil':
                Réptil.criarRéptil()
            elif animal == 'Peixe':
                Peixe.criarPeixe()
            elif animal == 'Ave':
                Ave.criarAve()
        elif teste2 == True:
            if animal == 'Mamífero':
                Mamífero.exibirAtributos()
            elif animal == 'Réptil':
                Réptil.exibirAtributos()
            elif animal == 'Peixe':
                Peixe.exibirAtributos()
            elif animal == 'Ave':
                Ave.exibirAtributos()
    @classmethod
    def criarAnimal(cls):
        while True:
            if not Animal.listaanimal:
                print('Não é possível criar mais animais.')
                break
            else:
                print('Só é possível criar um animal por vez. Qual animal deseja criar?: ')
                print(Animal.listaanimal)
                animal = input('Escolha: ')
                animal = animal.title()
                if animal in Animal.listaanimal:
                    try:
                        Animal.checarAnimal(animal, teste1=True)
                    except:
                        print('Houve um erro na criação do animal.')
                    else:
                        global contador
                        contador += 1
                        Animal.listaanimal.remove(animal)
                        Animal.animaiscriados[contador].append(animal)
                        print(f'{animal} criado com sucesso.')
                        break
                else:
                    print('Digite os animais de dentro da lista. ')

    @staticmethod
    def menu():
        selecionado = None
        while True:
            print('SELECIONADO:', selecionado)
            print('[1] Criar animal')
            print('[2] Selecionar animal')
            print('[3] Mostrar atributos')
            print('[4] Sair do programa')
            opção = input('Opção: ')
            if opção == '1':
                Animal.criarAnimal()
            elif opção == '2':
                testel = []
                for c in range(1, 5):
                    if not Animal.animaiscriados[c]:
                        testel.append(False)
                    else:
                        testel.append(True)
                        global vertrue
                        vertrue = 'sim'
                if vertrue == 'sim':
                    while True:
                        for k, v in Animal.animaiscriados.items():
                            print(k, v)
                        seleção = int(input('Digite o número do animal que deseja selecionar: '))
                        if seleção not in Animal.animaiscriados.keys():
                            print('Opção inválida.')
                        elif not Animal.animaiscriados[seleção]:
                            print('Não há animal nesta opção.')
                        else:
                            selecionado = Animal.animaiscriados[seleção][0]
                            print(selecionado)
                            break
                else:
                    print('Crie animais primeiro.')
            elif opção == '3':
                if selecionado == None:
                    print('Selecione um animal.')
                else:
                    Animal.checarAnimal(selecionado, teste2=True)
            elif opção == '4':
                print('Até logo!')
                break
            else: print('Opção inválida.')


class Mamífero(Animal):
    def __init__(self, peso, idade, membros, corPelo):
        Animal.__init__(self, peso, idade, membros)
        self.corPelo = corPelo

    def criarMamífero():
        peso = float(input('Peso: '))
        idade = int(input('Idade: '))
        membros = int(input('Membros: '))
        corpelo = input('Cor do pelo: ')
        global m1
        m1 = Mamífero(peso, idade, membros, corpelo)

    def exibirAtributos():
        print(f'Peso: {m1.peso}')
        print(f'idade: {m1.idade}')
        print(f'Membros: {m1.membros}')
        print(f'Cor do pelo: {m1.corPelo}')


class Réptil(Animal):
    def __init__(self, peso, idade, membros, corEscama):
        Animal.__init__(self, peso, idade, membros)
        self.corEscama = corEscama

    def criarRéptil():
        peso = float(input('Peso: '))
        idade = int(input('Idade: '))
        membros = int(input('Membros: '))
        corescama = input('Cor da escama: ')
        global r1
        r1 = Réptil(peso, idade, membros, corescama)

    def exibirAtributos():
        print(f'Peso: {r1.peso}')
        print(f'idade: {r1.idade}')
        print(f'Membros: {r1.membros}')
        print(f'Cor da escama: {r1.corEscama}')


class Peixe(Animal):
    def __init__(self, peso, idade, membros, corEscama):
        Animal.__init__(self, peso, idade, membros)
        self.corEscama = corEscama

    def criarPeixe():
        peso = float(input('Peso: '))
        idade = int(input('Idade: '))
        membros = int(input('Membros: '))
        corescama = input('Cor da escama: ')
        global p1
        p1 = Peixe(peso, idade, membros, corescama)

    def exibirAtributos():
        print(f'Peso: {p1.peso}')
        print(f'idade: {p1.idade}')
        print(f'Membros: {p1.membros}')
        print(f'Cor da escama: {p1.corEscama}')

class Ave(Animal):
    def __init__(self, peso, idade, membros, corPena):
        Animal.__init__(self, peso, idade, membros)
        self.corPena = corPena

    def criarAve():
        peso = float(input('Peso: '))
        idade = int(input('Idade: '))
        membros = int(input('Membros: '))
        corpena = input('Cor da escama: ')
        global a1
        a1 = Ave(peso, idade, membros, corpena)

    def exibirAtributos():
        print(f'Peso: {a1.peso}')
        print(f'idade: {a1.idade}')
        print(f'Membros: {a1.membros}')
        print(f'Cor da pena: {a1.corPena}')

Animal.menu()