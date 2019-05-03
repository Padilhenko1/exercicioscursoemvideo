#ler o comprimento de 3 retas
#diga se elas podem ou não formar um triângulo
a=float(input('Lado a: '))
b=float(input('Lado b: '))
c=float(input('Lado c: '))
if (b-c)<a<(b+c): #fator para um triângulo existir googleit
    print('É possivel formar um triângulo.')
else:
    print('Não é possivel formar um triângulo.')