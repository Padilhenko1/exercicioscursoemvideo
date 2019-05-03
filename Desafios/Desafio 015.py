dia=int(input("Quantos dias você ficou com o carro alugado: "))
km=float(input('Quantos km você percorreu: '))
pagar=(dia*60)+(km*0.15)
print('Você tem que pagar R${}.'.format(pagar))