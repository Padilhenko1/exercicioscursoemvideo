#ler o peso de 5 pesssoas.
#no final mostrar qual foi o maior e qual foi o menor
m1=0
maior=0
menor=0
for i in range (1,6):
    peso=float(input('{}º Peso: '.format(i)))
    if i == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        elif peso<menor:
            menor=peso
print('O maior peso lido foi {} Kg'.format(maior))
print('O menor peso foi {} Kg'.format(menor))
