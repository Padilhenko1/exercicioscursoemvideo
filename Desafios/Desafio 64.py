'''Ler vários numeros inteiros, só parar quando digitar 999
no final mostrar quantos números foram digitados
e a soma entre eles'''
n1 = 0
n2 = 0
c = 0
print ('Digite quantos números quiser até 998.')
while n1 <999:
    n1=int(input('Entre com o número: '))
    c=c+1
    n2 = n1 + n2
print ('Você digitou {} vezes.'.format(c))
print ('A soma de todos os números digitados é {}.'.format(n2))