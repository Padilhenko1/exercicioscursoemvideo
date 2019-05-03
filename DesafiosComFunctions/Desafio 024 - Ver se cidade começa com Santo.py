def analisar(cidade):
    cidade=cidade.split()
    if cidade[0]=='SANTO':
        return True
    else:
        return False

cidade=input('Digite o nome de sua cidade: ').strip().upper()

if analisar(cidade) == True:
    print('Sua cidade começa com Santo.')

else:
    print('Sua cidade não começa com Santo.')