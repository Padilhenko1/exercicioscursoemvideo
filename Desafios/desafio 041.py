#ler o ano de nascimento e mostrar a categoria de acordo com a idade
#ate 9 mirim, ate 14 infantil, ate 19 junior, ate 20 senior e acima de 20 master
from datetime import date
atual=date.today().year
ano=int(input('Ano de Nascimento?'))
ano=atual-ano
print('O atleta tem {} anos.'.format(ano))
if ano <=9:
    print('Categoria:\033[1m MIRIM.\033[m')
elif ano>=9 and ano<=14:
    print('Categoria:\033[1m INFANTIL.\033[m')
elif ano>=14 and ano<=19:
    print('Categoria:\033[1m JUNIOR.\033[m')
elif ano>=19 and ano<=20:
    print ('Categoria:\033[1m SÊNIOR.\033[m')
else:
    print ('Gategoria:\033[1m MASTER.\033[m')