import re

def tirar_tags(string):
    return re.sub(r'<.+?>', '', string)


def colocar_tags(string):
    pegando_grupos = re.findall('(\w+).(\w+).(\w+).(\w+)', string)
    for grupo in pegando_grupos:
        um, dois, tres, quatro = grupo
    return f'<p>{um}</p> <p>{dois}</p> <p>{tres}</p> <div>{quatro}</div>'

print('Tirando Tags:', end=' ')
print(tirar_tags('<p>Expressões</p> <p>Regulares</p> <p>São</p> <div>Eficientes</div>'))
print('Colocando Tags:', end=' ')
print(colocar_tags('Expressões Regulares São Eficientes'))

