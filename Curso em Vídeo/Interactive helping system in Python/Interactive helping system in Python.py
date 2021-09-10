def mural():
    print('\033[0;30;44m~'*30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('~' * 30)
    print('\033[m')
def acesso(x):
    print('\033[0;30;41m~' * 50)
    print(f'  Acessando o manual do comando "{x}"')
    print('~' * 50)
    print('\033[m')
    print('\033[0;30;45m')
    help(x)
    print('\033[m')
def fim():
    print('\033[0;30;43m~'*30)
    print(f'{"ATÉ LOGO":^30}')
    print('~' * 30)
    print('\033[m')
##Programa Principal
mural()
while True:
    fun = input('Função ou Biblioteca > ')
    fun = fun.lower()
    if fun == 'fim':
        break
    acesso(fun)
fim()

