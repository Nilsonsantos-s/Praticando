num = int(input('Digite um número: '))
divisores = int()
for c in range(1, num+1):
    if num%c == 0:
        divisores = divisores + 1
if divisores == 2:
    print('O número é primo!')
else:
    print('O número não é primo.')

