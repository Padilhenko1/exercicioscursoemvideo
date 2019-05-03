n1=int(input('Entre com um número :'))
n2=int(input('Entre com outro número : '))
s=n1+n2
p=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2

print('A soma dos números é {} \n A multiplicação dos números é {}\n A divisão dos números é \n{:.3f} A divisão inteira dos números é {:.2f}\n  {} elevado a {} é {}' .format (s,p,d,di,n1,n2,e))