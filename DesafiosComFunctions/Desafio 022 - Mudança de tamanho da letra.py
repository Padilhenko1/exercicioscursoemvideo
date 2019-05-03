def maiusculo (x):
    return x.upper()

def minusculo(x):
    return x.lower()

def contar_letras_nome_todo(x):
    x=len(x)-x.count(' ')
    return x

def contar_letras_nome(x):
    x=x.split()
    return x

nome=str(input('Digite seu nome todo: ')).strip()
maiusc=maiusculo(nome)
minusc=minusculo(nome)
contar_todo=contar_letras_nome_todo(nome)
primeiro=contar_letras_nome(nome)

print(maiusc)
print(minusc)
print(contar_letras_nome_todo(nome))
print(len(primeiro[0]))