'''Ler vários números inteiros, no final mostrar a média
entre todos eles  dizer qual foi o maior e menor valor lido
programa pergunta se quer continuar ou não'''
soma=0
maior=0
menor=0
c=0
esc = 'S'
while esc=='S':
    n1=int(input('Entre com um número: '))
    soma=n1+soma
    c=c+1
    esc=str(input('Quer continuar?[S/N]')).upper()
    if c==1:
        maior=n1
        menor=n1
    else:
        if n1>maior:
            maior=n1
        elif n1<menor:
            menor=n1
media=(soma/c)
print ('Você digitou {} números.'.format(c))
print ('A média entre eles é {}'.format(media))
print ('O maior número lido foi {}'.format(maior))
print ('O menor número lido foi {}'.format(menor))
