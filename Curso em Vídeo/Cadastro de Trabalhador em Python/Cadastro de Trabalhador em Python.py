nome = input('Nome: ')
ano = int(input('Ano de Nascimento: '))
carteira = int(input('Carteira de Trabalho (0 não tem): '))
if carteira != 0:
    anocon =  int(input('Ano de Contratação: '))
    salario = float(input('Salário: R$'))
print('=' * 50)
print('== DADOS TRABALHISTAS ==')
if carteira != 0:
    dados = {'Nome': nome,
            'Idade': 2021-ano,
            'CTPS': carteira,
            'Contratação': anocon,
            'Salário': salario,
            'Aposentadoria': (anocon + 35) - 2000}
else:
    dados = {'Nome': nome,
             'Idade': 2021 - ano,
             'CTPS': carteira}
for k, v in dados.items():
    print(f'{k}: {v}')
