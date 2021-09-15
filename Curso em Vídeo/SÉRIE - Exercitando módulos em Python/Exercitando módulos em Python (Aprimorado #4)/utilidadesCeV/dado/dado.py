def leiaDinheiro(x):
    while True:
        p = input(x)
        if ',' in p:
            p = p.replace(',', '.')
        if p.isnumeric() == False:
            teste = '.' in p
            if teste == False:
                print(f'ERRO: "{p}" é um preço inválido!')
            else:
                p = float(p)
                return p
                break
        else:
            p = float(p)
            return p
            break

