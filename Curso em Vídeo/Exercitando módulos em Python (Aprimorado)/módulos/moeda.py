def aumentar(num, porc):
    resultado = num+((num*porc) / 100)
    return resultado

def diminuir(num, porc):
    resultado = num-((num*porc) / 100)
    return resultado

def dobro(num):
    resultado = num*2
    return resultado

def metade(num):
    resultado = num/2
    return resultado

def moeda(valor):
    valor = str(valor)
    string = 'R$' + valor
    return string


