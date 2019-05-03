#ler duas notas e informar se foi reprovado abaixo de 5
#recuperação entre 5 e 6,9 e aprovado acima de 7
from time import sleep
n1=float(input('Nota de v1: '))
n2=float(input('Nota de v2: '))
print('Analisando...')
sleep(2)
media=(n1+n2)/2
print('Sua média é de {:.2f}.'.format(media))
if media<5:
    print('Você foi reprovado.')
elif 5 <= media <7:
    print('Você está de recuperação.')
else:
    print('Você foi aprovado.')
