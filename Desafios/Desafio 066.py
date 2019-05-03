#ler varios números
#só parar quando digitar 999
#o final mostrar quantos números foram digitados e qual foi a soma
#desconsiderando o 999
numero = False
c=soma=0
while not numero:
    n=int(input('Digite um número [999 para encerrar]: '))
    if n==999:
        break
    else:
        c+=1
        soma=n+soma
print(f'Foram digitados {c} números.')
print(f'A soma dos números digitados é {soma}.')