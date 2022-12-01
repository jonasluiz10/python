import math
CO = float(input('digite o comprimento do  cateto oposto: '))
CA = float(input('digite o comprimento do cateto adjacente '))
hip = math.hypot(CO, CA)
print('O comprimento da hipotenusa será de {:.2f}'.format(hip))