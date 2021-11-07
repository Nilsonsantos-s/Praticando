def menu():
    ano1 = int(input())
    ano2 = int(input())
    if ano1 == 0 and ano2 == 0:
        exit()
    lista = []
    listab = []
    intervalo = 0
    if ano1 > ano2:
        print('O primeiro ano deve ser menor que o segundo.')
        menu()
    else:
        dif = ano2-ano1
    lista.append(ano1)
    for contador in range(1, dif+1):
        ano1 += 1
        lista.append(ano1)
    for ano in lista:
        if ano%4 == 0 and ano%100 == 0 and ano%400 == 0:
            listab.append(ano)
            intervalo += 1
        elif ano%4 == 0 and ano%100 != 0:
            listab.append(ano)
            intervalo += 1
    for anob in listab:
        print(anob, end=' ')
    print(f'\n{intervalo}')
    menu()

menu()
