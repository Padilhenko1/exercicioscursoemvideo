#programa jogar par ou impar com o computador
#o jogo para quando o jogador perder
#mostrar o total de vitorias que ele conseguiu
from random import randint
verdade = False
c=0
while not verdade:
    print ('--'*15)
    print ('Vamos brincar de par ou impar?')
    print ('--'*15)
    comp=randint(0,10)
    n=int(input('Qual seu número?'))
    soma = comp + n
    escolha=str(input('Par ou Impar?[P/I]: ')).upper().strip()
    if soma%2==0 and escolha=='P':
        print (f'O computador escolheu {comp}.')
        print (f'{comp} + {n} = {soma}')
        print ('Você ganhou,deu par!!')
        print('---'*10)
        print ('Vamos de novo.')
        c=c+1
    elif soma%2!=0 and escolha=='I':
        print (f'O computador escolheu {comp}')
        print(f'{comp} + {n} = {soma}')
        print ('Você ganhou,deu impar!!')
        print ('Vamos de novo.')
        c=c+1
    elif escolha not in 'IiPp':
        verdade= False
    elif soma%2!=0 and escolha=='P':
        print (f'O computador escolheu {comp}')
        print(f'A soma de {comp} + {n} = {soma} ')
        print('Deu impar')
        print('Você perdeu.')
        break
    elif soma%2==0 and escolha =='I':
        print (f'O computador escolheu {comp}')
        print (f'A soma de {comp} + {n} = {soma} ')
        print ('Deu par')
        print ('Você perdeu')
print ('FIM')
input()
