#achar hipotenusa
from math import sqrt,hypot
op=float(input('Cateto oposto: '))
ad=float(input('Cateto adjacente: '))
#hip= sqrt(op**2+ad**2)
hip=hypot(op,ad)
print('Hipotenusa = {}' .format(hip))
