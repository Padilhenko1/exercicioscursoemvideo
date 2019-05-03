#ler uma frase
#quantas vezes aparece 'A'
#em qual posição aparece a primeira
#em qual posição aparece a ultima
frase=str(input('Escreva uma frase: ')).lower().strip() #strip tira espaços indesejados
print('Sua frase tem {} (as)'.format(frase.count('a')))
print('O primeiro A aparece na posição {}'.format(frase.find('a')+1))
print('O ultimo A aparece na posição {}'.format(frase.rfind('a')+1))