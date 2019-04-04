frase = str(input('Informe uma frase:')).strip().upper()#em maiusculo so pro Python, so pra reconhecer A ou a
print('Existem: {} letras A, cuja primeira ocorrência aparece na {}ª posição e por'
      ' último na ª'.format(frase.count('A'), frase.find('A')+1), frase.rfind('A')+1) #rfind procura a partir do fim
