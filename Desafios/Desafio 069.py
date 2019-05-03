#ler a idade e sexo de varias pessoas
#a cada pessoa cadastrada,programa pergunta se quer continuar
#a-quantas pessoas tem mais de 18 anos
#b-quantos homens foram cadastrados
#c-quantas mulheres tem menos de 20 anos
ver=False
c=mu=ho=0

while not ver:
    sexo=str(input('Sexo [M/F] : ')).upper().strip()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F] : ')).upper().strip()
        if sexo not in 'MmFf':
            print ('Sexo inválido')
    if sexo == 'M':
        ho=ho+1
    idade = int(input('Idade: '))
    if idade >=18:
        c=c+1
    elif sexo == 'F' and idade<20:
        mu=mu+1
    cont=str(input('Quer continuar [S/N]: ')).upper().strip()
    if cont in 'Nn':
        break
print (f'{c} pessoas com mais de 18 anos foram cadastradas.')
print (f'{ho} homens foram cadastrados.')
print (f'{mu} mulheres com menos de 20 anos foram cadastradas.')

