# ler nome, idade e sexo de 4 pessoas
# média de idade do grupo
# nome do homem mais velho
# quantas mulheres tem menos de 20 anos
'''nomema= ''
nomeme = ''
maior = 0
menor = 0
sexo = ''
contid = 0
velho = ''
contm=0
for i in range (1,5):
    print ('---------{}ª Pessoa--------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str (input ('Sexo [M/F]')).upper().strip()
    contid += idade #somando as idades
    if sexo == 'F' and idade < 20:
        contm = contm + 1 #contando número de mulheres com menos de 20 anos
    if i == 1: #primeira pessoa receber maior idade,nome,etç
        maior = idade
        nomema = nome
        menor = idade
        nomeme = nome
        if sexo == 'M':
            velho = nome
    else:
        if idade > maior:
            maior = idade
            nomema=nome
            if sexo == 'M':
                velho = nome
        else:
            meno = idade
            nomeme = nome
media = contid / i
print ('Média de idade é {}'.format(media))
print ('{} é o homem mais velho com {} anos.'.format(velho,maior))
print ('Ao todo são {} mulheres com menos de 20 anos.'.format(contm))'''
somaidade = 0
médiaidade= 0
maioridadehomem=0
nomevelho=''
totmulher20=0
for i in range (1,5):
    print ('--------{}ª Pessoa--------'.format(i))
    nome = str (input('Nome: ')).strip()
    idade = int (input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade +=idade
    if i == 1 and sexo == 'M':
        maioridadehomem=idade
        nomevelho=nome
    if idade > maioridadehomem and sexo == 'M':
        maioridadehomem=idade
        nomevelho=nome
    if sexo == 'F' and idade < 20:
        totmulher20 = totmulher20 + 1

médiaidade=somaidade/i
print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))