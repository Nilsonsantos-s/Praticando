lista = []
for contador in range(1,6):
    numero = int(input('Digite o {}º número: '.format(contador)))
    lista.append(numero)
    for c2 in range (1, 5):
        for c3 in range(0, len(lista)):
            if c3 == len(lista)-1:
                None
            else:
                if lista[c3+1] < lista[c3]:
                    copiaitem = lista[c3+1]
                    lista[c3+1] = lista[c3]
                    lista[c3] = copiaitem
    posicao = lista.index(numero)
    if lista[contador-1] == numero:
        print('Foi adicionado ao final da lista')
    else:
        print('Foi adicionado na posição {} da lista'.format(lista.index(numero)))
print('Os valores digitados em ordem foram:', lista)