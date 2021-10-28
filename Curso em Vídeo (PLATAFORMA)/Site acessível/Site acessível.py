import urllib.request
try:
    print(urllib.request.urlopen("http://www.pudim.com.br").getcode())
except:
    print('Site não disponível no momento :(')
else:
    print('Site acessado com sucesso!')
