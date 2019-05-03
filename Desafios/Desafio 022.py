#Ler o nome completo da pessoa
#nome com todas as letras maiusculas
#Numero de letras no nome
#Quantas letras tem o primeiro nome
nome=str(input('Digite seu nome todo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
nomec=len(nome)-nome.count(' ') #exclui espaços vazio entre os nomes
print('Seu nome tem ao todo {} letras.'.format(nomec))
dividido=nome.split()
print('Seu primeiro nome é {} tem ao todo {} letras.' .format(dividido[0],len(dividido[0]))) #numero de letras primeiro nome