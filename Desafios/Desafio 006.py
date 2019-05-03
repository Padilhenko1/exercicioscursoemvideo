# Mostra o dobro, triplo e raiz quadrada de um número
n1 = int(input('Entre com um número: '))
print('O\033[;32m dobro desse número é \033[4;32m{}\033[m,o \033[;31m triplo é \033[4;31m{}\033[m e a \033[;34mraiz quadrada é \033[4;34m{:.2f}\033[m'.format(n1 * 2, n1 * 3, n1 ** (1 / 2)))
