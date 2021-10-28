string = input('Digite uma string qualquer: ')
tamanho = len(string)-1
copiaposzero = string[0]
copiaposult = string[tamanho]
string = string[1:tamanho]
print(copiaposult+string+copiaposzero)