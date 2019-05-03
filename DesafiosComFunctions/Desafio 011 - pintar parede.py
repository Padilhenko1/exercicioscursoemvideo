def pintura (x,y):
    area = x * y
    quant = area/2
    print (f'Área total de pintura é {area}.')
    print (f'Você deve usar {quant} litros de tinta para pintar.')
    return

n1=int(input('Largura da parede: '))
n2=int(input('Altura da parede: '))
pintura(n1,n2)