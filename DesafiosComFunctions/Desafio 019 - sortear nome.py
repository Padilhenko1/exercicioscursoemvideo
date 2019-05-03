import random

def listar (x):
   return lista.append(x)

def sortear(x):
    x=random.choice(x)
    return x

lista = []
n=int(input('Quer sortear quantos nomes? '))
for i in range (1,n+1):
    nome = str(input(f'Nome {i}: '))
    listar(nome)
print(f'O nome sorteado foi: {sortear(lista)}.')

