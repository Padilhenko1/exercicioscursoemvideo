#ler um nome e ver se tem Silva no nome
nome=str(input('Digite seu nome: ')).strip()
n=nome.lower().find('silva')
if n==-1:
    print('Seu nome não tem Silva.')
else:
    print('Seu nome tem Silva.')
