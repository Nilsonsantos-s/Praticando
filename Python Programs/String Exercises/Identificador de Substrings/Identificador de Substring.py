string = input('Digite uma string qualquer: ')
substring = input('Digite a substring: ')
resultado = str(substring in string)
if resultado == 'True':
    print('Substring está presente na string!')
else:
    print('Substring não foi encontrada em string!')
