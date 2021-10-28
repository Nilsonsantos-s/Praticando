n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1+n2)/2
if media < 5.0:
    print('Média: {:.1f}'.format(media))
    print('REPROVADO')
elif media >=5 and media < 7.0:
    print('Média: {:.1f}'.format(media))
    print('RECUPERAÇÃO')
elif media >= 7:
    print('Média: {:.1f}'.format(media))
    print('APROVADO! :)')
