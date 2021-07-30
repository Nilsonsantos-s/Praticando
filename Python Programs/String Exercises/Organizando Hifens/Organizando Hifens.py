frase = input('Digite uma frase com hifens: ')
while True:
    frasecomhifen = str('-' in frase)
    if frasecomhifen == 'False':
        frase = input('Frase sem hifens. Por favor, tente novamente: ')
    else:
        if frase[0] == '-' or frase[len(frase)-1] == '-':
            frase = input('Frase sem palavras compostas. Por favor, tente novamente: ')
        else:
            break
frasealterada = frase.replace('-', ' ')
listapalavras = frasealterada.split()
listaordenada = (sorted(listapalavras))
print('A frase em ordem alfabética fica: {}'.format('-'.join(listaordenada)))
