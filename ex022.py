nome = input('Informe seu nome completo:').lstrip()
print('Todo em maiúsculo: {}'.format(nome.upper()))
print('Todo em minusculo: {}'.format(nome.lower()))
print('Existem: {} letras no nome: '.format(len(nome) - nome.count(' ')))

print('No primeiro nome existem: {} letras'.format(nome.find(' ')))
#separa = nome.split() #dividindo string em substrings
#print('No primeiro nome ( {} ) existem: {} letras'.format(separa[0],len(separa[0])))
