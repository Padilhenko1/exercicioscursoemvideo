def analisar (numero):
    if (len(numero)==4):
        print (f'Unidade = {numero[3]}')
        print (f'Dezena = {numero[2]}')
        print (f'Centena = {numero[1]}')
        print (f'Milhar = {numero [0]}')
    elif (len(numero)==3):
        print(f'Unidade = {numero[2]}')
        print(f'Dezena = {numero[1]}')
        print(f'Centena = {numero[0]}')
    elif (len(numero)==2):
        print(f'Unidade = {numero[1]}')
        print(f'Dezena = {numero[0]}')
    elif (len(numero)==1):
        print (f'Unidade= {numero[0]}')
    else:
        print('Esse número é maior que 9999.')
    return

def analisar2(num):
    unidade = num // 1 % 10
    dezena = num // 10 % 10
    centena = num // 100 % 10
    milhar = num // 1000 % 10
    print('Unidade: {}'.format(unidade))
    print('Dezena: {}'.format(dezena))
    print('Centena: {}'.format(centena))
    print('Milhar: {}'.format(milhar))
    return


n=int(input('Digite um número: '))

analisar2(n)