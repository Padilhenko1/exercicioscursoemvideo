#escrever um número
#ver qual conversão o usuário quer, 1 binário, 2 octal e 3 hexadecimal
import time
num=int(input('Entre com um número: '))
print('''Converter para: 
[1] - Binário.
[2]- Octal.
[3]- Hexadecimal.''')
n=int(input('Quer que converta por: '))
print('Calculando...')
time.sleep(2)
if n==1:
    bina=bin(num)
    print('O binário de {} é {}.'.format(num,bina[2:]))
elif n==2:
    octa=oct(num)
    print('O octadecimal de {} é {}.'.format(num,octa[2:]))
elif n==3:
    hexa=hex(num)
    print('O hexadecimal de {} é {}.'.format(num,hexa[2:]))
else:
    print ('Opção inválida.Tente novamente.')