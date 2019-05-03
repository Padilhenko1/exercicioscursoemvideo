#ler o nome e preço de varios produtos
#perguntar se quer continuar
#a-qual o total gasto na compra
#b-quantos produtos custam mais de 1000 reais
#c-qual nome do produto mais barato
true=False
mil=0
barato=''
valorbarato=c=0
while not true:
    produto=str(input('Produto: '))
    valor=float(input('Valor : '))
    escolha=input('Quer continuar [S/N]: ').upper().strip()
    c=c+1
    if valor>=1000:
        mil+=1
    elif c==1:
        barato=produto
    else:
        if valor>valorbarato:
            barato=produto
    if escolha=='N':
        break

print(f'{mil} produtos custam mais de 1000 reais.')
print(f'{barato} é o produto mais barato.')