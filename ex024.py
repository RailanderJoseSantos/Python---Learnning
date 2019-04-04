cidade = input('Informe o nome de sua cidade:').strip() #remove espaços
cidade = cidade.split()
print('Cidade começa com SANTO ? {}'.format('SANTO' in cidade[0]))
#print(cidade[:5].upper()=='SANTO')
