#um programa que calcule a soma entre todos os números impares que são multiplos de 3
#no intervalo de 1 até 500
s=0
c=0
for i in range (1,501,2):
      if i%3==0:
        c=c+1
        s=s+i
print ('A soma de todos os {} números impares, multiplos de 3,entre 1 e 500 é {}.'.format(c,s))

