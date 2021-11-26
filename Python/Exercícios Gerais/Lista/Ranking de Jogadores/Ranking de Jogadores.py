lista = []
contador = 0
while True:
    dado = int(input())
    if dado != -1:
        lista.append(dado)
    else:
        lista.append(dado)
        break
tamanho = len(lista)
lista.sort()


try:
    if lista[tamanho-1] != -1:
        print(f'Primeiro lugar: {lista[tamanho-1]}')
    else:
        print(f'Primeiro lugar: NÃO HÁ JOGADOR')
except:
    print(f'Primeiro lugar: NÃO HÁ JOGADOR')
try:
    if lista[tamanho-2] != -1:
        print(f'Segundo lugar: {lista[tamanho-2]}')
    else:
        exit()
except:
    print(f'Segundo lugar: NÃO HÁ JOGADOR')
    print(f'Terceiro lugar: NÃO HÁ JOGADOR')
    exit()
else:
    try:
        if lista[tamanho-3] != -1:
            print(f'Terceiro lugar: {lista[tamanho-3]}')
        else:
            print(f'Terceiro lugar: NÃO HÁ JOGADOR')
    except:
        print(f'Terceiro lugar: NÃO HÁ JOGADOR')