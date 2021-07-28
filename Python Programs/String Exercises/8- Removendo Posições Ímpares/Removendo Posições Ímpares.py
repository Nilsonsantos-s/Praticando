frase = input('Digite uma frase qualquer: ')
tamanho = len(frase)
fr = str()
for c in range(0, tamanho):
   if c == 0:
       fr += frase[c]
   if c> 0 and c%2 == 0:
       fr += frase[c] 
print(fr)