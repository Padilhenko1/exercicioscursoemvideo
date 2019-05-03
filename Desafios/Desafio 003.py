n1 = int(input('\033[0;33mDigite um número:\033[m '))
n2 = int(input('\033[0;31mDigite outro número:\033[m '))
s = n1 + n2
print('A soma de \033[0;33m{}\033[m e \033[;31m{}\033[m é no valor de \033[;32m{}'.format(n1, n2, s))
