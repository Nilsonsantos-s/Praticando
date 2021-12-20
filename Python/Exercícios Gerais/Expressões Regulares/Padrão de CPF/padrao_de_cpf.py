import re


def tirar_padrao_cpf(cpf):
    teste = re.findall(r'([\d]*).([\d]*).([\d]*).([\d]*)', cpf)
    for grupo in teste:
        um, dois, tres, quatro = grupo
    return um+dois+tres+quatro


def colocar_padrao_cpf(cpf):
    teste = re.findall(r'([\d]{3})([\d]{3})([\d]{3})([\d]{2})', cpf)
    for grupo in teste:
        um, dois, tres, quatro = grupo
    cpf_final = um+'.'+dois+'.'+tres+'-'+quatro
    return cpf_final

print(colocar_padrao_cpf('12345678911'))
print(tirar_padrao_cpf('358.457.621-99'))
