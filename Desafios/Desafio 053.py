#ler uma frase e diga se é PALINDROMO
frase = str (input('Digite uma frase: ')).strip().upper()
palavras=frase.split() #separar as palavras da frase
junto=''.join(palavras) #junta as palavras
inverso=''
'''for letra in range(len(junto)-1,-1,-1):
    inverso=inverso + junto[letra]'''
if inverso==junto:
    print('Temos um palindromo.')
else:
    print('A frase digitada não é um palindromo.')
print(junto,inverso)