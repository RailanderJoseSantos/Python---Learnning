nome = str(input('Informe seu nome completo:')).strip()
nome = nome.split() # divide em substrings
qttString = len(nome) -1 # passa quantas strings foram criadas
print('Primeiro nome: {}, último nome: {}'.format(nome[0], nome[qttString]))


