#refazer o desafio 009 da tabuada com o laço for.
print ('|||TABUADA|||')
n=int(input('Digite o número da tabuada: '))
for i in range(0,11):
    m=n*i
    print ('{} x {} = {}'.format(n,i,m))