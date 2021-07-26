pritermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = int(10)
resposta = int(1)
maistermo = int()
numerodetermos = int()
while contador > 1:
    if contador == 10:
        print(pritermo)
        numerodetermos += 1
    pritermo = pritermo + razao
    print(pritermo)
    numerodetermos += 1
    contador = contador - 1
while resposta != 0:
    resposta = int(input('Quantos termos você quer mostrar a mais?: '))
    contador = resposta
    while contador > 0:
        pritermo = pritermo + razao
        print(pritermo)
        numerodetermos += 1
        contador = contador -1
if resposta == 0:
    print('Progressão finalizada com {} termos mostrados.'.format(numerodetermos))

