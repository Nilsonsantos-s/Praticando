tupla = (1, 2, 3, 4, 5)
num = int(input('Digite um número qualquer: '))
resultado = str(num in tupla)
if resultado == 'True':
    print(num, 'está contido na tupla.')
else:
    print(num, 'não está contido na tupla.')