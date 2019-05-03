#ler a velocidade de um carro
#Se for acima de 80, dizer que foi multado
#Multa vai ser 7 reais a cada km acima do limite
veloc=float(input('Velocidade do carro: '))
if veloc>80.0:
    multa=(veloc-80.0)*7
    print('Você ultrapassou a velocidade.')
    print('Sua multa será de: R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança.')