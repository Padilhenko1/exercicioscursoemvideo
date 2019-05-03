# ler 3 numeros e mostrar qual é o maior e qual é o menor
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
import math

if n1 > n2 and n1 > n3:
    if n3 > n2:
        print('Maior: {}\nMenor: {}'.format(n1, n2))
    else:
        print('Maior: {}\nMenor: {}.'.format(n1, n3))

elif n2 > n1 and n2 > n3:
    if n3 > n1:
        print('Maior: {}\nMenor: {}'.format(n2, n1))
    else:
        print('Maior: {}\nMenor: {}.'.format(n2, n3))
elif n3 > n1 and n3 > n2:
    if n2 > n1:
        print('Maior: {}\nMenor: {}'.format(n3, n1))
    else:
        print('Maior: {}\nMenor: {}'.format(n3, n2))
