def analisar (nome):
    analise='silva' in nome.lower()
    if analise==True:
        print('Seu nome tem Silva.')
    else:
        print('Seu nome não tem Silva.')
    return analise


n=str(input('Qual o seu nome: ')).strip()

analisar(n)