from time import sleep
def maior(* num):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    contador = 0
    for numero in num:
        print(numero, end=' ')
        sleep(0.40)
        contador += 1
        if maior < numero:
            maior = numero
    print(f'--- Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


