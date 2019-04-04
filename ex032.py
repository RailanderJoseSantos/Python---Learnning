from datetime import date
ano = int(input('Que ano você quer analisar (digite 0 para o ano atual) ? '))
if ano == 0:
    ano = date.today().year
print('{} é um ano bissexto!'.format(ano) if ano % 4 == 0 else '{} não é ano bissexto!'.format(ano))

