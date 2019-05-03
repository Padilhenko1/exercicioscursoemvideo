#ler um nome completo
#mostrar o primeiro e o ultimo nome separadamente
nome=str(input('Escreva seu nome todo: '\033[0;33;44m)).strip()
primeiro,*meio,fim=nome.split() #todas as palavras exceto a primeira e a ultima vão para a variavel middle.
#print(primeiro,fim)
print('Seu primeiro nome é {}'.format(primeiro))
print('Seu ultimo nome é {}'.format(fim))

