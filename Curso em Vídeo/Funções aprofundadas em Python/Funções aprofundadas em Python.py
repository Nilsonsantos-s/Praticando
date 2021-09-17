def leiaInt(x):
    while True:
        try:
            n = int(input(x))
        except (ValueError, TypeError):
            print(f'Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print(f'O usuário optou por não digitar este número.')
        else:
            return n

def leiaFloat(x):
    while True:
        try:
            f = float(input(x))
        except (ValueError, TypeError):
            print(f'Digite um número real válido.')
        except KeyboardInterrupt:
            print(f'O usuário optou por não digitar este número.')
        else:
            return f

#Programa Principal
n = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {f}')