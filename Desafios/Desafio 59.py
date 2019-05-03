'''Calculadora
ler dois valores
1 - somar
2 - multiplicar
3 - mostrar qual é maior
4 - entrar com novos números
5 - sair'''
n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número; '))
choice=0
while choice != 5:
    print('-=-'*10)
    print('1-Somar')
    print('2-Multiplicar')
    print('3-Mostrar qual é o maior valor')
    print('4-Entrar com novos números')
    print('5-Sair')
    print('-=-'*10)
    choice=int(input('>>>>>>>>>Qual sua opção?'))
    print('  ')
    if choice==1:
        soma=n1+n2
        print ('{} + {} = {}.'.format(n1,n2,soma))
        print(' ')
    elif choice==2:
        mult=n1*n2
        print('{} x {} = {}'.format(n1,n2,mult))
        print(' ')
    elif choice==3:
        if n1>n2:
            print('Entre {} e {} o maior é {}'.format(n1,n2,n1))
            print(' ')
        else:
            print('{} e {} o maior é {}'.format(n1,n2,n2))
            print(' ')
    elif choice==4:
        n1=int(input('Digite o primeiro número novamente: '))
        n2=int(input('Digite o segundo número novamente: '))
