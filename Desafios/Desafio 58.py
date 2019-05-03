'''Melhorar o jogo 28, onde só finaliza quando acertar
e mostrar quantas tentativas foram feitas'''
'''import random, os
import time
print ('-=-'*20)
print ('Sou seu computador... \nAcabei de pensar em um número de de 0 a 10.')
print ('Será que você consegue adivinhar qual foi? ')
print ('-=-'*20)
nc=random.randint(0,10) #numero computador randomiza entre 1 e 10
r=0 #resposta
c=0 #contador
while r != nc:
    r=int(input('Qual seu palpite? '))
    c += 1
    if r!=nc:
        print ('EROOOOUU!')
        print ('Tente novamente!')
        print ('    ')
print ('Parabéns, o número era {}.'.format(nc))
print ('Você acertou com {} tentativas.'.format(c))
input ('Finalizar')'''

from random import randint
rc=randint(0,10) #resposta computador
print('-='*20)
print('Eu sou o seu computador e acabei de pensar em um número de 0 a 10.')
print('Será que você consegue advinhar qual foi?')
print('-='*20)
acertou=False
c=0
while not acertou:
    rj=int(input('Qual o seu palpite: '))
    c=c+1
    if rj==rc:
        acertou=True
    else:
        if rj<rc:
            print('Mais... tente novamente.')
        elif rj>rc:
            print('Menos... tente novamente.')
#print('O número era {}'.format(rc))
print(f'O número era {rc}')
print('Você acertou com {} tentativas. Parabéns'.format(c))