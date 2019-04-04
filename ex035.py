m1 = float(input('Informe a reta 1: '))
m2 = float(input('Informe a reta 2: '))
m3 = float(input('Informe a reta 3: '))

if m1 < m2 + m3 and  m2 < m1 + m3 and m3 < m1 + m2:
    print('É possível formar um triângulo.')
else:
    print('Impossível formar um triângulo, pois as retas somas de duas retas são maiores que uma outra!')
