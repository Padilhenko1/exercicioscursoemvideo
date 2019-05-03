#ler dois números
#comparar e mostrar : qual dos dois é maior ou se são iguais
n1=float(input('Primeiro número: '))
n2=float(input('Segundo número: '))
if n1>n2:
    print ('{} é maior que {}.'.format(n1,n2))
elif n2>n1:
    print ('{} é maior que {}.'.format(n2,n1))
else:
    print('Os dois números são iguais.')