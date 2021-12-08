string = "Practice Problems to Drill List Comprehension in Your Head."

"""
1-
numeros_divisiveis_por_8 = [numero for numero in range(1, 1001) if numero % 8 == 0]
print(numeros_divisiveis_por_8)
"""

"""
2-
numeros_que_contem_seis = [numero for numero in range(1, 1001) if '6' in str(numero)]
print(numeros_que_contem_seis)
"""

"""
3-
contagem_de_espacos = [string.count(' ')]
print(contagem_de_espacos)
"""

"""
4-
palavras_menor_que_5letras = [palavra for palavra in string.split() if len(palavra) < 5]
print(palavras_menor_que_5letras)
"""

"""
5-
numeros_divisiveis = [numero for numero in range(1, 1001) if True in [True for divisor in range(2, 10) if numero % divisor == 0]]
print(numeros_divisiveis)
"""
