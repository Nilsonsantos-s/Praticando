##OBS:
##Tuplas são imutáveis, então você não consegue adicionar um item
##a uma tupla da seguinte maneira:
## tupla = 'milkshake', 'lanche'
## tupla[2] = 'suco'
##mas é possível fazer de um outro jeito:

tupla = ()
resposta = 's'
print('A tupla está vazia:', tupla)
while resposta == 's':
    additem = input('Digite um item para adicionar à tupla: ')
    if additem.isnumeric() == True:
        additem = int(additem)
    tupla = tupla + (additem,)
    print('A tupla é:', tupla)
    resposta = input('Deseja adicionar mais um item? [S/N]: ')
    resposta = resposta.lower()
print('A tupla é:', tupla)
