def hipo(x,y):
    from math import hypot
    hip = hypot(x,y)
    print(f'Hipotenusa = {hip:.2f}')
    return

op=int(input('Cateto oposto: '))
ad=int(input('Cateto adjacente: '))
hipo (op,ad)