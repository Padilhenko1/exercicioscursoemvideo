def truncar (x):
    from math import trunc
    inteiro=trunc(x)
    print(f'O número inteiro de {x} é {inteiro}.')
    return


n=float(input('Digite um número: '))
truncar(n)