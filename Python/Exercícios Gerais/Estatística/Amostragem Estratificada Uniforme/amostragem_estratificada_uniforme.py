import random
al_sexomasculino = {'Michael': 0, 'Fabiano': 0, 'Thiago': 0, 'Lucas': 0, 'Matheus': 0, 'Jeferson': 0, 'Hiago': 0, 'Lázaro': 0, 'Maurício': 0,
                    'Nilton': 0, 'Nazar': 0, 'Gabriel': 0, 'Lucca': 0, 'Agrim': 0, 'Nicolas': 0, 'Mário': 0, 'Nivaldo': 0, 'Wesley': 0, 'José': 0,
                    'Kelvin': 0, 'Jimmy': 0, 'Henrique': 0, 'Leandro': 0, 'Leonardo': 0, 'André': 0}

al_sexofeminino = {'Priscila': 0, 'Rebeca': 0, 'Bianca': 0, 'Rosana': 0, 'Crystal': 0, 'Angela': 0, 'Ágata': 0, 'Jacyara': 0, 'Lais': 0, 'Carolina': 0,
                   'Stacy': 0, 'Chloe': 0, 'Letícia': 0, 'Tiffany': 0, 'Cátia': 0, 'Naomi': 0}

for key in al_sexomasculino.keys():
    al_sexomasculino[key] = random.randint(10, 70)
for key in al_sexofeminino.keys():
    al_sexofeminino[key] = random.randint(10, 70)

print('Quantidade total de elementos da população:',
      len(al_sexomasculino) + len(al_sexofeminino))
print('Quantidade desejada de elementos na amostra: 10')
print('Uniformidade dos elementos de cada estrato: 5 de cada')
print('-'*40+'AMOSTRA'+'-'*40)
print(random.choices(list(al_sexofeminino.items()), k=5))
print(random.choices(list(al_sexomasculino.items()), k=5))
print('-'*87)
