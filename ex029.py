vel = float(input('Informe a velocidade: '))
#condicao simples - unico if
if vel > 80:
    print('Você foi multado!')
    valor = (vel - 80) * 7
    print('Valor da multa: R${:.2f}'.format(valor))
print('Bom dia, dirija com segurança!')
