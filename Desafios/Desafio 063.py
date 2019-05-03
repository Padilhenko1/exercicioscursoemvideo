'''Ler um número n inteiro e mostrar os primeiros elementos de
uma sequencia de Fibonacci'''
print ('--'*11)
print ('SEQUÊNCIA DE FIBONACCI')
print ('--'*11)
n=int(input('Quantos termos você deseja? '))
p=0
fibo=1
ant1= 1
ant2=0
prox=0
print ('0',end=' => ')
while p<=n-1:
    print(fibo,end=' => ')
    fibo = ant1 + ant2
    if ant1<=fibo:
        ant2=ant1
        ant1=fibo
    p=p+1
print ('FIM')