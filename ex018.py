from math import radians, sin, cos, tan
n = float(input('Informe o valor do ângulo:'))
seno = sin(radians(n))
cosseno = cos(radians(n))
tang = tan(radians(n))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2}'.format(tang))
