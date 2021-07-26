import random
vitoria = int()
while True:
    print('='*20)
    num = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I]: ')
    print('='*20)
    escolha = escolha.lower()
    computador = random.randint(0,10)
    if (computador+num)%2 == 0:
        resultado = 'PAR'
    elif (computador+num)%2 == 1:
        resultado = 'ÍMPAR'
        print(f'O computador jogou {computador} e você {num}. Total de {computador+num} DEU {resultado}!')
    if escolha == 'p' and (num+computador)%2 == 0 or escolha == 'i' and (num+computador)%2 == 1:
        print('VITÓRIA!!!\nVamos jogar novamente!')
        vitoria = vitoria + 1
    elif escolha == 'p' and (num+computador)%2 != 0 or escolha == 'i' and (num+computador)%2 != 1:
        print('GAME OVER!')
        print(f'Você venceu {vitoria} vezes.')
        break


