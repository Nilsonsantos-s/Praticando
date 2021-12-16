numeros = [numero for numero in range(1, 21)]
numeros_pares = [numero for numero in range(1, 21) if numero % 2 == 0]
numeros_impares = [numero for numero in range(1, 21) if numero % 2 != 0]
print(f'{numeros}\n{numeros_pares}\n{numeros_impares}')
