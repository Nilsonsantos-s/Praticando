import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno é {:.2f} \nO cosseno é  {:.2f}\nO tangente é {:.2f}'.format(seno, cosseno, tangente))
