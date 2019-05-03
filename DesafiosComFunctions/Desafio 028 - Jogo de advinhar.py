import random

def sortear(x):
    y=random.randint(1,5)
    if x == y:
        print(f'O número sorteado foi: {y}')
        print('Parabéns, você acertou.')
    else:
        print(f'O número sorteado foi: {y}')
        print('Infelizmente você errou.')
    return x

numero=(int(input('Tente advinhar um número de 1 a 5: ')))

sortear(numero)
