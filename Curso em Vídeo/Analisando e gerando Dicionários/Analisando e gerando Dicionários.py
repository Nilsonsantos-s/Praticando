def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas
    :param sit: valor opcional (True/False), indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['Notas'] = num
    maiornota = 0
    cont = 0
    soma = 0
    for c in dados['Notas']:
        cont += 1
        soma += c
        if maiornota < c:
            maiornota = c
        if cont == 1:
            menornota = c
        if c < menornota:
            menornota = c
    media = round(soma/cont, 2)
    dados['Total'] = cont
    dados['Maior'] = maiornota
    dados['Menor'] = menornota
    dados['Média'] = media
    if media >= 7:
        resultado = 'BOA'
    elif media < 7 and media >= 5:
        resultado = 'RAZOÁVEL'
    else:
        resultado = 'RUIM'
    if sit == True:
        dados['Situação'] = resultado

    return(dados)



##Programa Principal:
resp = notas(0, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)