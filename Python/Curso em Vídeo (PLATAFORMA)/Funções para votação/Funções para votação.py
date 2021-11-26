def voto(ano):
    """
    :para ano: Ano digitado
    :return: Retorna quantos anos o usuário
             tem e se o seu voto é obrigatório, opcional ou negado.
    """
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade <= 70:
        print(f'Você tem {idade} anos.')
        print('Voto Obrigatório!')
    elif idade >= 16 and idade < 18 or idade > 70:
        print(f'Você tem {idade} anos.')
        print('Voto Optativo!')
    elif idade < 16:
        print(f'Você tem {idade} anos.')
        print('Não Vota!')

##Programa Principal
voto(2000)