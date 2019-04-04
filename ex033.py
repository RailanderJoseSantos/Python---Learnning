n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o psegundo número: '))
n3 = float(input('Informe o terceiro número: '))
'''
maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    #podera ser menor: n2 ou n3
    if n2 < n3:
        menor = n2
    else:
        menor = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    #podera ser menor: n1 ou n3
    if n1 < n3:
        menor = n1
    else:
        menor = n2
else:
    maior = n3
    #podera se menor: n1 ou n2
    if n1 < n2 and n1 < n3:
        menor = n1
    else:
        menor = n2
if maior ==  menor:
    print('Todos os números são iguais!')
else:
    print('Maior:{:.2f} Menor:{:.2f}'.format(maior, menor)) '''

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior:{:.2f} Menor:{:.2f}'.format(maior, menor))



