#simular o funcionamento de um caixa eletrônico
#iniciar perguntando qual valor a ser sacado
#quantas cédulas de cada valor serão entregues
#50,20,10 e 1
true=False
c50=c20=c10=c1=0
print ('----'*20)
print ('CAIXA ELETRÔNICO')
print ('----'*20)
sacar=int(input('Qual valor a ser sacado: R$ '))
sacar2=sacar
while sacar>0:
    if sacar>=50:
        sacar=sacar-50
        c50=c50+1
    elif sacar>=20:
        sacar=sacar-20
        c20=c20+1
    elif sacar>=10:
        sacar=sacar-10
        c10=c10+1
    elif sacar>=1:
        sacar=sacar-1
        c1=c1+1
print(f'Para sacar R${sacar2}.')
print(f'{c50} notas de 50 reais, {c20} notas de 20 reais, {c10} notas de 10 reais e {c1} notas de 1 real.')