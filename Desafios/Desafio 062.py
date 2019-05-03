'''Refazer o 61 e mostrar quantos termos a mais ainda quer'''
print ('Gerador de PA')
print('-=-'*10)
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da sua PA: '))
d=0
m=0
mais=-1
choice=1
soma=0
while d!=10:
    print (n, end =' => ')
    n = n + r
    d = d + 1
print('Pausa')
while mais!=0:
    print('')
    mais=int(input('Quantos termos você quer mais? '))
    m=0
    while m!=mais:
        print (n, end = ' => ')
        n = n + r
        m = m + 1
        soma = soma + 1
soma=10+soma
print ('Progressão finalizada com {} termos mostrados'.format(soma))