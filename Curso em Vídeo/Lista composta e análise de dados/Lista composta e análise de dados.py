listax = list()
listay = list()
contador = 0
maiorpeso = int()
menorpeso = int()
listamaiorpeso = list()
listamenorpeso = list()
while True:
    if contador == 0:
        nome = input('Nome: ')
        listax.append(nome)
        peso = float(input('Peso: '))
        listax.append(peso)
        listay.append(listax[:])
        pesoantes = listax[1]
        menorpeso = pesoantes
        maiorpeso = pesoantes
    else:
        pesoantes = listax[1]
        nome = input('Nome: ')
        listax[0] = nome
        peso = float(input('Peso: '))
        listax[1] = peso
        listay.append(listax[:])
        pesodepois = listax[1]
        if pesodepois > maiorpeso:
            maiorpeso = pesodepois
        if pesodepois < menorpeso:
            menorpeso = pesodepois
    resposta = input('Quer continuar? [S/N]: ')
    resposta = resposta.lower()
    if resposta == 'n':
        break
    if resposta != 's' and resposta != 'n':
        while resposta != 's' or resposta != 'n':
            print('Resposta inválida.')
            resposta = input('Quer continuar? [S/N]: ')
            resposta = resposta.lower()
            if resposta == 's' or resposta == 'n':
                break
    contador += 1
for c in range(0, len(listay)):
    for c2 in range(0,2):
        if listay[c][c2] == maiorpeso:
            listamaiorpeso.append(listay[c][c2-1])
        if listay[c][c2] == menorpeso:
            listamenorpeso.append(listay[c][c2-1])

print('O número de pessoas cadastradas é:', len(listay))
print('O maior peso foi de {}Kg. Peso de {}'.format(maiorpeso, listamaiorpeso))
print('O menor peso foi de {}Kg. Peso de {}'.format(menorpeso, listamenorpeso))
