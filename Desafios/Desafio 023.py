#Ler um numero de 0 a 9999 e mostre cada um dos digitos separados
n=input('Digite um número de 0 a 9999: ')
if (len(n)==4):
#unidade=n[3]
    print('Unidade: {}'.format(n[3]))
#dezena=n[2]
    print ('Dezena: {}'.format(n[2]))
#centena=n[1]
    print('Centena: {}'.format(n[1]))
#milhar=n[0]
    print('Milhar: {}'.format(n[0]))
elif (len(n)==3):
#unidade=n[2]
    print('Unidade: {} '.format(n[2]))
#dezena=n[1]
    print('Dezena: {}'.format(n[1]))
#centena=n[0]
    print('Centena: {}'.format(n[0]))
elif (len(n)==2):
#unidade=n[1]
    print('Unidade: {}'.format(n[1]))
#dezena=n[0]
    print('Dezena: {}'.format(n[0]))
else:
#unidade=n[0]
    print('Unidade: {}'.format(n[0]))