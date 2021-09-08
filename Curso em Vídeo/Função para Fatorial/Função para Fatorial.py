def fatorial(número, show=False):
    """
    :para número: O número a ser calculado
    :para show (opcional): True/False - Mostrar ou não a conta
    :return: Retorna o fatorial
    """
    resultado = 1
    for c in range(número, 0, -1):
        resultado *= c
        if show == True:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end='')
    if show == True:
        print(f' = {resultado}')
    else:
        print(resultado)


##Programa Principal
fatorial(5)