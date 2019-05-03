import random

def adicionar_na_lista(x):
    return lista.append(x)

def sortear_sequencia(x):
    random.shuffle(x)
    return x

lista = []

for i in range (1,4):
    nome=str(input(f'Nome {i}: '))
    adicionar_na_lista(nome)
print(f'A ordem de apresentação é : {sortear_sequencia(lista)}')