# ler um valor do produto
# condição de pagamento
# a vista dinheiro/cheque 10% desconto
# a vista cartão:5%, 2 x no cartão preço normal
# 3x ou mais : 20% de juros
valor = float(input('Valor do produto: R$'))
print('Qual a forma de pagamento? ')
print('1-Dinheiro\n2-Cheque\n3-Cartão')
a =int( (input('')))
if a == 1:
    valor = valor*0.9
    print('Você escolheu dinheiro a vista, ganha 10% de desconto.')
    print('Você deve pagar R${:.2f}.'.format(valor))
elif a==2:
    valor=valor*0.9
    print('Você escolheu cheque a vista, ganha 10% de desconto.')
    print('Você deve pagar R${:.2f}.'.format(valor))
else:
    d=int(input('Você quer dividir em quantas vezes: '))
    if d==1:
        valor=valor*0.95
        print('Pagando no cartão a vista,você ganha 5% de desconto.')
        print('Você deve pagar R${:.2f}.'.format(valor))
    elif d==2:
        valor=valor/d
        print('Você vai pagar {} parcelas de R${:.2f}.'.format(d,valor))
    elif d>=3:
        valor=(valor*1.2)/d
        print('Com juros de 20%.')
        print('Você vai pagar {} parecelas de R${:.2f}'.format(d,valor))