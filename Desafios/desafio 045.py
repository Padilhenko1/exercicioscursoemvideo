#fazer um jogo do jokenpô
import random
a=['Pedra','Papel','Tesoura']
a=random.choice(a)
b=int(input('1-Pedra\n2-Papel\n3-Terousa\n'))
if b==1 and a=='Pedra':
    print('Computador escolheu {}.'.format(a))
    print('Empatou.')
elif b==1 and a=='Tesoura':
    print('Computador escolheu {}.'.format(a))
    print('Você ganhou.')
elif b==1 and a=='Papel':
    print('Computador escolheu {}.'.format(a))
    print('Você perdeu.')
elif b==2 and a=='Pedra':
    print('Computador escolheu {}.'.format(a))
    print('Você ganhou.')
elif b==2 and a=='Papel':
    print ('Computador escolheu {}.'.format(a))
    print('Empatou.')
elif b==2 and a=='Tesoura':
    print('Computador escolheu {}.'.format(a))
    print('Você perdeu.')
elif b==3 and a=='Pedra':
    print('Computador escolheu {}.'.format(a))
    print('Você perdeu.')
elif b==3 and a=='Papel':
    print('Computador escolheu {}.'.format(a))
    print('Você ganhou.')
else:
    print('Computador escolheu {}.'.format(a))
    print('Empatou.')

n=input(('\n\n\n\nDigite algo para fechar:'))

