import datetime
def stringweekday():
    nsemana = atualdata.weekday()
    if nsemana == 0:
        return 'Segunda-feira'
    elif nsemana == 1:
        return 'Terça-feira'
    elif nsemana == 2:
        return 'Quarta-feira'
    elif nsemana == 3:
        return 'Quinta-feira'
    elif nsemana == 4:
        return 'Sexta-feira'
    elif nsemana == 5:
        return 'Sábado'
    elif nsemana == 6:
        return 'Domingo'

atualdata = datetime.datetime.today()
print(f'Dia atual: {atualdata.day}/{atualdata.month}/{atualdata.year} {atualdata.time()}')
print(f'Ano: {atualdata.year}')
print(f'Mês: {atualdata.strftime("%B")}')
print(f'Dia: {atualdata.day}')
print(f'Dia da semana: {stringweekday()}')
print(f'Dias do ano: {atualdata.strftime("%j")}')
print(f'Quantas semanas do ano: {atualdata.strftime("%H")}')

