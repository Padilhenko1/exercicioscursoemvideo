#quantidade de tinta para pintar parede
lar=float(input('Qual a altura da parede a ser pintada? '))
alt=float(input('Qual a largura da parede a ser pintada? '))
area=lar*alt
print ('A área total que você deve pintar é {} m²'.format(area))
quant=area/2
print ('Você deve usar {} litros de tinta para pintar esta parede.'.format(quant))
