'''Escrever um número e mostrar seu fatorial'''
n=int(input('Digite um número: '))
f=1
print ('Fatorial de {}! é : '.format(n))
while n !=1:
    print ('{}'.format(n),end= ' x ')
    f = f * n
    n=n-1
print ('1 = {}'.format(f))