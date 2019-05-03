nomema= ''
nomeme = ''
maior = 0
menor = 0
sexo = ''
contid = 0
velho = ''
contm=0
for i in range (1,5):
    print ('---------{}ª Pessoa--------'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str (input ('Sexo [M/F]')).upper()
    contid += idade
    if sexo == 'F' and idade < 20:
        contm = contm + 1
    if i == 1:
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
print ('Ao todo são {} mulheres com menos de 20 anos.'.format(contm))
