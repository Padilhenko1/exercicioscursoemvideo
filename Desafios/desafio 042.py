#refazer o desafio 35 e ver se o triângulo é equilátero, isósceles ou escaleno
#equilatero todos os lados iguais, isoceles dois lados iguais e escaleno todos os lados diferentes
a=float(input('Lado a: '))
b=float(input('Lado b: '))
c=float(input('Lado c: '))
if b-c<a<b+c:
    if a==b==c:
        print('Triangulo equilátero (Três lados iguais).')
    elif a==b or a==c or b==c:
        print('Triangulo isóceles (Dois lados iguais).')
    else:
        print('Triângulo escaleno (Três lados diferentes).')
else:
    print('Triângulo impossível.')