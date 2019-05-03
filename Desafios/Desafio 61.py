'''Refazer desafio 52, ler o primeiro e ter a razão
mostrando os 10 primeiros termos'''
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Qual a razão da sua PA: '))
d=0
while d !=10:
    print(n , end = ' => ')
    d = d + 1
    n = n + r
print('FIM')