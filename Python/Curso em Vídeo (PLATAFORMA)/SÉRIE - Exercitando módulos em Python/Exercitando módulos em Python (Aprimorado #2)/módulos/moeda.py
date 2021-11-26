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


