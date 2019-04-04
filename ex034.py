sal = float(input('Informe o salário R$'))
if sal > 1250:
    au = sal * 0.1
else:
    au = sal * 0.15
print('Salário atualizado: R${:.2f}, obteve aumento de: R${:.2f}'.format(au + sal, au))
