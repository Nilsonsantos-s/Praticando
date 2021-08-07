string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
t = len(string1)-1
res = bool()
resu = str()
for c in range(0, t+1):
    resu = str(string1[c] in string2)
    if resu == 'False':
        res = 'False'
if res == 'False':
    print('Não são anagramas.')
else:
    print('São anagramas.')