from time import sleep
def contador(início, fim, passo):
    c = início
    if início < fim:
        while c < fim+1:
            print(c, end=' ')
            sleep(0.30)
            c += passo
        print('FIM!')
    elif início > fim:
        while c > fim-1:
            print(c, end=' ')
            sleep(0.30)
            c = c - passo
        print('FIM!')
#Programa Principal
print('-'*50)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('-'*50)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('-'*50)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
pas = abs(pas)
if pas == 0:
    pas = 1
print('-'*50)
print(f'Contagem de {ini} até {fi} de {pas} em {pas}')
contador(ini, fi, pas)



