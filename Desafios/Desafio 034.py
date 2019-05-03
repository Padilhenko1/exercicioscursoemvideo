#ler salario e dar aumento
#aumento de 10% a superior 1250,00
#aumento de 15% a inferior de 1250,00
salario=float(input('Entre com seu salário: '))
if salario>=1250.00:
    print('Você receberá um aumento de 10%.')
    salario=salario*1.10
    print('Seu novo salário será de R${:.2f}'.format(salario))
else:
    print('Você receberá um aumento de 15%.')
    salario=salario*1.15
    print('Seu novo salário será de R${:.2f}'.format(salario))