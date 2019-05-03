#ler o peso e altura e calcular o IMC
#abaixo de 18.5 - abaixo do peso
#abaixo de 25-peso ideal
#abaixo de 30 - sobrepeso
#abaixo de 40 - obesidade
#cima de 40- obesidade mórbida
peso=float(input('Qual o seu peso: '))
altura=float(input('Qual a sua altura: '))
imc=peso/(altura**2)
if imc <=18.5:
    print ('IMC {:.1f}, você está abaixo do peso.'.format(imc))
elif imc >=18.5 and imc<=25:
    print('IMC {:.1f}, você está com peso ideal.'.format(imc))
elif imc>=25 and imc<=30:
    print('IMC {:.1f}, você esta com sobrepeso.'.format(imc))
elif imc>=30 and imc<=40:
    print('IMC {:.1f}, você está opeso.')
else:
    print('IMC {:.1f}, você está com obesidade mórbida.')