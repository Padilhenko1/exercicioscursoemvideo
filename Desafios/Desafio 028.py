#fazer o programa pensar em 0 a 5
#usuario tentar descobrir o numero
import random
from time import sleep #fazer esperar tempo
import colorsys
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente advinhar!')
print('-=-'*20)
n=random.randint(0,5)
t=int(input('Tente advinhar o número de 0 a 5: '))
print('Processando...')
sleep(3) #tempo de espera
print('O número sorteado foi: {}'.format(n))
if t==n:
    print('Parabéns, você acertou ')
else:
    print('Que pena,você errou')