import re


def tirar_padrao_telefone(telefone):
    grupos = re.findall(r'.(\d+).(\d+).(\d+)', telefone)
    for grupo in grupos:
        um, dois, tres = grupo
    telefone_sem_padrao = um+dois+tres
    return telefone_sem_padrao

def colocar_padrao_telefone(telefone):
    grupos = re.findall(r'(\d{2})(\d{4})(\d{4})', telefone)
    for grupo in grupos:
        um, dois, tres = grupo
    telefone_com_padrao = f'({um}){dois}-{tres}'
    return telefone_com_padrao

print('Colocando padrão:', colocar_padrao_telefone('1135678932'))
print('Tirando padrão:', tirar_padrao_telefone('(11)3567-8932'))



