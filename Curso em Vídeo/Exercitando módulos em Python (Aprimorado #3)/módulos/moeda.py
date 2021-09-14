def aumentar(num, porc, log=False):
    resultado = num+((num*porc) / 100)
    if log == True:
        resultado = str(resultado)
        resultado = 'R$'+resultado
    return resultado

def diminuir(num, porc, log=False):
    resultado = num-((num*porc) / 100)
    if log == True:
        resultado = str(resultado)
        resultado = 'R$'+resultado
    return resultado

def dobro(num, log=False):
    resultado = num*2
    if log == True:
        resultado = str(resultado)
        resultado = 'R$'+resultado
    return resultado

def metade(num, log=False):
    resultado = num/2
    if log == True:
        resultado = str(resultado)
        resultado = 'R$'+resultado
    return resultado

def moeda(valor):
    valor = str(valor)
    string = 'R$' + valor
    return string

def resumo(num, aum, red):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":>22}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20} {moeda(num):<20}')
    print(f'{"Dobro do preço:":<20} {dobro(num, True):<20}')
    print(f'{"Metade do preço:":<20} {metade(num, True):<20}')
    print(f'{aum}%{" de aumento:":<17} {aumentar(num, aum, True)}')
    print(f'{red}%{" de redução:":<17} {diminuir(num, red, True)}')
    print('-' * 30)


