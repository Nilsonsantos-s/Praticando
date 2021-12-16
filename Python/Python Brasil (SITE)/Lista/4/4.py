import re
letras = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
numero_consoantes = 0
for letra in letras:
    if letra not in re.findall(r'[aeiou]', letra):
        print(letra)
        numero_consoantes += 1
print('Número de Consoantes:', numero_consoantes)