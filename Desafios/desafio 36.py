# ler o valor da casa
# ler o salario do comprador
# quantos anos vai pagar
# mensal não pode ser 30% a mais do que o salário, senão vai ser negado
preco = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
ano = int(input('Quantos anos financiando?: '))
mensal = ano * 12
prest = preco / mensal
trint = salario * 0.3
if prest > trint:
    print('\033[1;31mNegócio negado\033[m')
    print('O valor mensal ficaria em {:.2f}, acima de 30% do seu salário.'.format(prest))
else:
    print('\033[1;32mEmprestimo Concedido\033[m')
    print('Você vai pagar mensalmente R${:.2f}.'.format(prest))
