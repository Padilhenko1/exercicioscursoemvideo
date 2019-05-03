# ler 6 numeros inteiros e mostrar a soma somente dos pares.
s = 0
contador=0
contp=0
for i in range(1, 7):
    n = int(input('Digite o {}º número: '.format(i)))
    contador = contador + 1
    if n % 2 == 0:
        s = s + n
        contp=contp+1
print('Dos {} números digitados,{} são pares e a soma deles é {}.'.format(contador,contp,s))
