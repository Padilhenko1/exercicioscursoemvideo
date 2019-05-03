# ler o primeiro termo e a razão de uma PA.
# Mostrar os 10 primeiros termos dessa progressão
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
d=p+(10-1)*r
for i in range(p,d+r,r):
    print (i, end=' => ')
print('FIM')