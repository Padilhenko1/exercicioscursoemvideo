n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
print('1-Soma')
print('2-Subtração')
print('3-Multiplicação')
print('4-Divisão')
def soma(x,y):
    return x + y
def subtracao(x,y):
    return x - y
def multi(x,y):
    return x * y
def divisao (x,y):
    return x/y

while True:
    pergunta=str(input('Qual opção: '))
    if pergunta == '1':
        resultado = soma(n1,n2)
        break
    elif pergunta =='2':
        resultado = subtracao(n1,n2)
        break
    elif pergunta =='3':
        resultado = multi(n1,n2)
        break
    elif pergunta =='4':
        resultado = divisao(n1,n2)
        break
print (resultado)