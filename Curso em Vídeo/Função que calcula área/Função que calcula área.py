def área(largura, comprimento):
    print('Controle de Terrenos')
    print('---------------------')
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    x = comprimento * largura
    print(f'Área: {x}m²')

área(2,5)