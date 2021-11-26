from time import sleep
dados = {}
lista = []
listaitem = []

##Funções---
def adicionarChave():
    while True:
        chave = input('Digite uma chave: ')
        lista.append(chave)
        escolha = input('Deseja adicionar mais chaves? [S/N]: ')
        escolha = escolha.lower()
        while escolha != 'n' and escolha != 's':
            print('Opção inválida.')
            escolha = input('Deseja adicionar mais chaves? [S/N]: ')
            escolha = escolha.lower()
        if escolha == 'n':
            break

def adicionarItem():
    print('-'*30)
    while True:
        print(lista)
        chave = input('Selecione uma chave: ')
        if chave not in lista:
            print(f'{chave} não está na lista')
            sleep(1)
        else:
            break
    while True:
        item = input('Digite um item: ')
        listaitem.append(item)
        escolha = input(f'Deseja adicionar mais um item à chave "{chave}"? [S/N]: ')
        escolha = escolha.lower()
        while escolha != 'n' and escolha != 's':
            print('Opção inválida.')
            escolha = input(f'Deseja adicionar mais um item à chave "{chave}"? [S/N]: ')
            escolha = escolha.lower()
        if escolha == 'n':
            dados[chave] = tuple(listaitem)
            listaitem.clear()
            break

def mostrarDados():
    if not dados:
        print('O dicionário ainda está vazio. Crie chaves e adicione itens primeiro.')
        voltar = input('Pressione Enter para voltar ao Menu Principal ')
    else:
        print(dados)
        voltar = input('Pressione Enter para voltar ao Menu Principal ')

def menu():
    print(f'{"Construção de Dicionário":>28}')
    while True:
        print('-'*30)
        print('[1] Adicionar chaves')
        print('[2] Adicionar itens')
        print('[3] Mostrar dados')
        print('[4] Sair do programa')
        print('-'*30)
        opção = input('Digite uma opção: ')
        if opção == '1':
            adicionarChave()
        elif opção == '2':
            adicionarItem()
        elif opção == '3':
            mostrarDados()
        elif opção == '4':
            print('Até logo!')
            break
        else:
            print('Opção inválida!')
            sleep(1)

##Programa Principal---
menu()



