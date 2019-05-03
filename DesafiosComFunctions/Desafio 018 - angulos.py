def angulo (x):
    import math
    sen = math.sin(math.radians(x))
    cos = math.cos(math.radians(x))
    tang= math.tan(math.radians(x))
    print(f'Seu seno é {sen:.2f}')
    print(f'Seu cosseno é {cos:.2f}')
    print(f'Sua tangente é {tang:.2f}')
    return

anglo=int(input('Angulo: '))
angulo (anglo)