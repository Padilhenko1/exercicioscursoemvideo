#ler um ano e mostrar se é bissexto
import time,datetime
ano=int(input('Qual ano quer analisar?\nSe quiser o ano atual,digite 0. '))
if ano==0:
    ano=datetime.date.today().year #importa o ano atual da máquina
print('Analisando...')
time.sleep(2)
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('{} é ano bissexto'.format(ano))

    #if ano%400==0 and ano%100=:
        #print('{} é ano bissexto'.format(ano))
else:
    print('{} não é ano bissexto'.format(ano))