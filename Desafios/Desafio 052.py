# ler um número inteiro e diga se é ou não um número primo
n = int(input('Digite um número e verifique se é primo: '))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end=' ')
        c = c + 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(i), end=' ')
print('\033[m\nO número {} é divisível {} vezes.'.format(n, c))
if c > 2:
    print('\033[m\nPor isso o número {} não é primo.'.format(n))
else:
    print('\033[m\nPor isso o número {} é primo.'.format(n))
