cel=float(input('Temperatura em ºC: '))
kel=cel+273
fahr=(1.8*cel)+32
print('A temperatura {}ºC equivale a {}K e {:.2f}F'.format(cel,kel,fahr))