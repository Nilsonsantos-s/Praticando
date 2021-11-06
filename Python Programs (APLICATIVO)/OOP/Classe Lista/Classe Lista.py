class Lista:
    def __init__(self, lista):
        self.lista = lista

    def adicionarItem(self):
        item = input('Digite um item: ')
        if item.isnumeric():
            item = int(item)
        self.lista.append(item)

    def deletarItem(self):
        if not self.lista:
            return cor('A lista está vazia.', amarelo=True)
        while True:
            self.mostrarLista()
            item = input('Digite um item: ')
            if item not in self.lista:
                cor(f'O item {item} não está na lista.', vermelho=True)
            else:
                if item.isnumeric():
                    item = int(item)
                self.lista.remove(item)
                break

    def mostrarLista(self):
        return cor(self.lista, amarelo=True)


    @staticmethod
    def menu():
        while True:
            cor('[1]Adicionar item', azul=True)
            cor('[2]Deletar item', azul=True)
            cor('[3]Mostrar lista', azul=True)
            cor('[4]Sair do programa', azul=True)
            try:
                opção = int(input('Opção: '))
            except ValueError:
                cor('Opção inválida!', vermelho=True)
            else:
                if opção == 1:
                    l1.adicionarItem()
                elif opção == 2:
                    l1.deletarItem()
                elif opção == 3:
                    l1.mostrarLista()
                elif opção == 4:
                    cor('Volte sempre! :)', amarelo=True)
                    break
                else:
                    cor('Opção inválida!', vermelho=True)

def cor(string, vermelho=False, azul=False, amarelo=False):
    if vermelho == True:
        print(f'\033[1;31m{string}\033[m')
    elif azul == True:
        print(f'\033[1;34m{string}\033[m')
    elif amarelo == True:
        print(f'\033[1;33m{string}\033[m')
    else:
        print(f'\033[1;38m{string}\033[m')


l1 = Lista([])
Lista.menu()



