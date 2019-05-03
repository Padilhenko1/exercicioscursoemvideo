import math
num=(float(input('Entre com um angulo: ')))
sen=math.sin(math.radians(num))
cos=math.cos(math.radians(num))
tang=math.tan(math.radians(num))
print('Seu cosseno é {:.2f}.\nSeu seno é {:.2f}.\nSua tangente é {:.2f}.'.format(cos,sen,tang))