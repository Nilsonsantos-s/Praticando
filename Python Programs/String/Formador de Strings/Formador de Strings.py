frase = input('Digite uma frase com pelo menos 4 caracteres: ')
while True:
    if len(frase) < 4:
        frase = input('Digite uma frase com pelo menos 4 caracteres: ')
    else:
        break
primeirasletras = ''
ultimasletras = ''
for c in range(0, len(frase)):
    if c == 0 or c == 1:
        primeirasletras += frase[c]
    if c ==len(frase)-1 or c == (len(frase)-1)-1:
        ultimasletras += frase[c]
print(' A nova string formada é: {}'.format(primeirasletras+ultimasletras))
