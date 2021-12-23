<h2>Tags HTML</h2>

Faça um programa que tenha duas funções:

* tirar_tags(string) 	       #  Retorna a string com as tags 
* colocar_tags(string)       # Retorna a string sem as tags

OBS:

Utilize como referência a seguinte string:

```
'<p>Expressões</p> <p>Regulares</p> <p>São</p> <div>Eficientes</div>'
```



<u>Exemplos</u>: 

```
print(tirar_tags('<p>Expressões</p> <p>Regulares</p> <p>São</p> <div>Eficientes</div>'))
```

OUTPUT: Expressões Regulares São Eficientes



```
print(colocar_tags('Expressões Regulares São Eficientes'))
```

OUTPUT:

```
<p>Expressões</p> <p>Regulares</p> <p>São</p> <div>Eficientes</div>
```

