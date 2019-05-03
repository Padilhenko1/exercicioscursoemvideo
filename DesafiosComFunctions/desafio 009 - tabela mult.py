def tabela (x):
    for i in range (1,11):
        mult=x*i
        print(f'{x} x {i} = {mult}')
    return 
n1=int(input('Número para tabuada: '))
tabela(n1)