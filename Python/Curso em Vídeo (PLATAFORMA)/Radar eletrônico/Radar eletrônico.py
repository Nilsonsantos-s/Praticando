velocidade = int(input('Digite a velocidade km/h de um carro em movimento: '))
print('A velocidade é {}km/h.'.format(velocidade), end=' ')
if velocidade>80:
    print('O carro foi multado!')
    multa = (velocidade-80)*7
    print('A multa é de {} reais'.format(multa))
