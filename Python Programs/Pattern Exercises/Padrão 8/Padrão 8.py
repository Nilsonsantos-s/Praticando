a1 = 1
soma = a1+a1
for c in range(1, 9):
    if c == 1:
        print(a1)
    elif c == 2:
        print('{:<3} {}'.format(soma, soma//2))
        soma = soma*2
    elif c == 3:
        print('{:<3} {:<3} {}'.format(soma, soma//2,  soma//4))
        soma = soma * 2
    elif c == 4:
        print('{:<3} {:<3} {:<3} {}'.format(soma, soma//2, soma//4, soma//8))
        soma = soma * 2
    elif c == 5:
        print('{:<3} {:<3} {:<3} {:<3} {}'.format(soma, soma // 2, soma // 4, soma // 8, soma//16))
        soma = soma * 2
    elif c == 6:
        print('{:<3} {:<3} {:<3} {:<3} {:<3} {}'.format(soma, soma // 2, soma // 4, soma // 8, soma // 16, soma// 32))
        soma = soma * 2
    elif c == 7:
        print('{:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {}'.format(soma, soma // 2, soma // 4, soma // 8, soma // 16, soma // 32, soma//64))
        soma = soma * 2
    elif c == 8:
        print('{:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {}'.format(soma, soma // 2, soma // 4, soma // 8, soma // 16, soma // 32, soma // 64, soma// 128))
        soma = soma * 2