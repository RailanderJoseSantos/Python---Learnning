km = float(input('Informe quantos Km foram rodados:'))
dias = int(input('Informe quantos dias o carro ficou alugado:'))
total = (dias * 60) + (0.15 * km)
print('Total: R${:.2f}'.format(total))
