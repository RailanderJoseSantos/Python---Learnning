dist = float(input('Informe a distância da viagem: '))
if dist <= 200:
    p = dist * 0.50
else:
    p = dist * 0.45
print('Valor da passagem: R${:.2f}'.format(p))
