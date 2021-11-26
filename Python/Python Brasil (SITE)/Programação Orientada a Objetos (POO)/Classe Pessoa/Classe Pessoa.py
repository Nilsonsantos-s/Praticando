##Classe ---
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.altura += 0.5
        else:
            self.idade += 1

    def Engordar(self):
        self.peso += 1

    def Emagrecer(self):
        self.peso -= 1

    def Crescer(self):
        self.altura += 0.5

##Funções ---
def menu():
    print('-'*40)
    print(f'{p1.nome:^38}')
    print('-' * 40)
    print(f'Idade: {p1.idade}')
    print(f'Peso: {p1.peso:.0f}')
    print(f'Altura: {p1.altura:.2f}')
    print('-' * 40)
    print('[1] Envelhecer\n[2] Engordar\n[3] Emagrecer\n[4] Crescer\n[5] Sair do Programa')
    escolha = int(input('Opção: '))
    if escolha == 1:
        try:
            p1.Envelhecer()
        except:
            print('ERRO! Ocorreu um problema na hora de envelhecer!')
        else:
            print('Envelheceu com sucesso!')
        finally:
            menu()
    elif escolha == 2:
        try:
            p1.Engordar()
        except:
            print('ERRO! Ocorreu um problema na hora de engordar!')
        else:
            print('Engordou com sucesso!')
        finally:
            menu()
    elif escolha == 3:
        try:
            p1.Emagrecer()
        except:
            print('ERRO! Ocorreu um problema na hora de emagrecer!')
        else:
            print('Emagreceu com sucesso!')
        finally:
            menu()
    elif escolha == 4:
        try:
            p1.Crescer()
        except:
            print('ERRO! Ocorreu um problema na hora de crescer!')
        else:
            print('Cresceu com sucesso!')
        finally:
            menu()
    elif escolha == 5:
        print('---- Até logo! ----')
    else:
        print('Digite uma opção válida!')
        menu()


##Programa principal ---
nome = input('Nome: ')
while nome.isalpha() == False:
    nome = input('O nome só pode conter letras: ')
while True:
    try:
        idade = int(input('Idade: '))
    except ValueError:
        print('ERRO! Tipo inválido!')
    else:
        break
while True:
    try:
        peso = float(input('Peso: '))
    except ValueError:
        print('ERRO! Tipo inválido!')
    else:
        break
while True:
    try:
        altura = float(input('Altura: '))
    except ValueError:
        print('ERRO! Tipo inválido!')
    else:
        break
p1 = Pessoa(nome, idade, peso, altura)
menu()





