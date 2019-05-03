#leia a idade
#informa se ela ainda vai se alistar, se é hora de alistar ou se ja passou da hora
#informar o tempo se passou ou se falta alistar
from datetime import date
atual=date.today().year
ano=int(input('Ano de nascimento: '))
idade=atual-ano
print('Você tem {} anos.'.format(idade))
if idade==18:
    print ('Você está no ano que tem que se alistar.')
elif idade >18:
    temp=idade-18
    time=atual-temp
    print('Você ja deveria ter se alistado.')
    print('Você passou do tempo de alistamento por {} anos.'.format(temp))
    print('Seu alistamento foi em {}.'.format(time))
else:
    temp=18-idade
    time=atual+temp
    print('Você ainda não precisa de se alistar, mas precisará daqui à {} anos.'.format(temp))
    print('Seu alistamento será em {}.'.format(time))