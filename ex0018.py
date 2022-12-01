from math import radians, sin, cos, tan
ang = float(input('digite um ângulo: '))
sen = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('o angulo é de: {}'.format(ang))
print('o seno será de {:.2f} o cosseno será de {:.2f} e a tangente será de {:.2f}'.format(sen, cosseno, tangente))