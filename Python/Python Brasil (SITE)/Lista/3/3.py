notas = [1, 5, 8, 3]
for pos, nota in enumerate(notas):
    print(f'Nota {pos+1}: {nota}')
media = sum(notas) / len(notas)
print('Média:', media)