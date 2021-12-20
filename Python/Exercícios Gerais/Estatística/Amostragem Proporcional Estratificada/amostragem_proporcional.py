import random
print('AMOSTRAGEM PROPORCIONAL ESTRATIFICADA')
print('-'*40)
al_sexomasculino = {'Michael', 'Fabiano', 'Thiago', 'Lucas', 'Matheus', 'Jeferson', 'Hiago', 'Lázaro', 'Maurício',
                    'Nilton', 'Nazar', 'Gabriel', 'Lucca', 'Agrim', 'Nicolas', 'Mário', 'Nivaldo', 'Wesley', 'José',
                    'Kelvin', 'Jimmy', 'Henrique', 'Leandro', 'Leonardo', 'André'}

al_sexofeminino = {'Priscila', 'Rebeca', 'Bianca', 'Rosana', 'Crystal', 'Angela', 'Ágata', 'Jacyara', 'Lais', 'Carolina',
                   'Stacy', 'Chloe', 'Letícia', 'Tiffany', 'Cátia', 'Naomi'}

total_alunos = len(al_sexomasculino.union(al_sexofeminino))
total_al_masculino = len(al_sexomasculino)
total_al_feminino = len(al_sexofeminino)
total_amostra = 10
div_amostra_aluno_totais = total_amostra / total_alunos
masc_pos_proporcao = round(total_al_masculino * div_amostra_aluno_totais)
fem_pos_proporcao = round(total_al_feminino * div_amostra_aluno_totais)
print('Número de alunos:', total_alunos)
print('Total planejado da amostra:', total_amostra)
print('Número de alunos do sexo masculino:', total_al_masculino)
print('Número de alunos do sexo feminino:', total_al_feminino)
print('Total de alunos do sexo masculino após a proporção:', masc_pos_proporcao)
print('Total de alunos do sexo feminino após a proporção:', fem_pos_proporcao)
amostra_al_masculino = random.choices(list(al_sexomasculino), k=masc_pos_proporcao)
amostra_al_feminino = random.choices(list(al_sexofeminino), k=fem_pos_proporcao)
print('AMOSTRA:', amostra_al_masculino + amostra_al_feminino)
