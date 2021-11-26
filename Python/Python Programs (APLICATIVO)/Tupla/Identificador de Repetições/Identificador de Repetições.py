tupla = (1, 2, 2, 4, 5, 6, 6, 4)
repetidos = str()
for numerox in tupla:
    contador = 0
    for numeroy in tupla:
        if numeroy == numerox:
            contador += 1
            if contador > 1:
                if str(numeroy) in repetidos:
                    None
                else:
                    repetidos = repetidos + str(numerox) + ' '
print('A tupla é:', tupla)
print('Os números repetidos são:', repetidos)



