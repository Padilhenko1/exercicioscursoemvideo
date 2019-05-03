n1=int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s=n1+n2 #somar os dois números
p=n1*n2 #multiplicar os dois numeros
d=n1/n2 #dividir os dois numeros
di=n1//n2 #dar a divisão inteira
e=n1**n2 #potencia
print ('A dos dois números é {}, \n o produto é {} e a divisão é {:.3f}' .format(s,p,d), end='. ')
print ('A divisão inteira é {} e a potência é {}' .format(di, e))

#\n quebra a linha e ,end=' ' faz continuar na mesma linha