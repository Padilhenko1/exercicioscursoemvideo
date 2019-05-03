#ler o ano de nascimento de 7 pessoas
#no final dizer quantas ja são maiores de idade e quantas não são
import datetime
ma=0
me=0
for i in range (0,7):
    ano = int(input('Ano de nascimento: '))
    idade=datetime.date.today().year-ano
    if idade>=18:
        ma=ma+1
    else:
        me=me+1
print('{} são maiores de idade e {} são menores de idade.'.format(ma,me))