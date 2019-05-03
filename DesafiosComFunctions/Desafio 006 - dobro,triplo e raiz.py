import math

def dobro(x):
    return 2*x
def triplo(x):
    return 3*x
def raiz(x):
    return math.sqrt(x)

n1=int(input('Entre com um número: '))
print(f'O dobro de {n1} = {dobro(n1)}')
print(f'O triplo de {n1} = {triplo(n1)}')
print(f'A raiz de {n1} = {raiz(n1):.2f}')
