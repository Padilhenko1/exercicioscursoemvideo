'''Ler o sexo, mas aceitar somente M ou F, caso digite errado
pedir para digitar novamente'''

'''sexo = ''
print ('------Digite o seu sexo-------')
print ('[M]/[F]')
while sexo !='M' and sexo !='F':
    sexo=str(input ('Digite o seu sexo: ')).upper()
    if sexo !='M' and sexo !='F':
        print ('Digitou errado, digite novamente.')
    if sexo=='M':
        print ('Sexo Masculino,registrado com sucesso.')
    elif sexo =='F':
        print ('Sexo Feminino,registrado com sucesso.')
print('Fim') '''
sexo=str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo=str(input('Dados invalidos, digite nocamente [M/F]: '))
print ('Sexo {} registrado com sucesso.'.format(sexo))
