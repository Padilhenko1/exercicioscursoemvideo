frase=('Eu gosto de hamburguer')
print(frase[3::4])
print(frase[1:10:2]) #pega as letras de 1 até 9 pulando de 2 em 2

#analise

#analisar string
frase=('Eu gosto de hamburguer')
print (len(frase)) #tamanho da frase

print (frase.count('o',0,13)) #contar o numero de letras
print (frase.find('ost')) #encontrar a letra
print (frase.find('Android')) #retorna -1 pois nao encontrou na frase
print ('hamburguer'in frase) #retorna True ou False

#Transformação
frase=('Eu gosto de hamburguer')
print(frase)

print(frase.replace('hamburguer','xburguer')) #troca a palavra da frase

print(frase.upper()) #coloca as frases em maiusculo
print(frase.lower()) #coloca a frase em minusculo
print(frase.capitalize()) #só a primeira letra fica maiuscula
print(frase.title()) #coloca só as primeiras caracteres das primeiras palavras em maiusculo
frase2=('    Eu gosto de lanche   ')
print(frase2)
print(frase2.strip()) #elimina os espaços vazios no final e no fim
print(frase2.rstrip()) #remove somente espaço a direita
print(frase2.lstrip()) #remove espaço da esquerda

#Divisão

frasediv=('Curso em vídeo de python')
print(frasediv.split()) #gera uma lista de cada palavra da frase
print('-'.join(frasediv.split())) #junta as palavras separadas pelo split com hífen