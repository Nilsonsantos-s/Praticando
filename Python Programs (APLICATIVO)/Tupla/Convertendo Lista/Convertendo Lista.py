lista = ['uva', 'morango']
print('A lista é', lista)
tupla = ()
for fruta in lista:
    tupla = tupla + (fruta,)
lista = tupla
print('A tupla é:', lista)
