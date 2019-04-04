from random import randint
from time import  sleep
n = randint(0, 5)
print('-=-'*50)
print('Vou pensar em um número entre 0 a 5, tente adivinhar... ')
print('-=-'*50)
nu = int(input('Qual o número: '))
print('Processando...')
if nu > 5 or nu < 0:
    print('Deve ser entre 0 a 5!!')
else:
    if n == nu:
        print('Você venceu!')
    else:
        print('Você perdeu, meu número foi {} e não {}'.format(n, nu))
print('-=-'*50)

