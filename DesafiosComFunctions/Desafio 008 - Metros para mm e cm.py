def mm (x):
    mm= x*1000
    return mm
def cm (x):
    cm = x*100
    return cm


n1=float(input('Entre com o valor em metros: '))
mm=mm(n1)
cm=cm(n1)
print(f'{n1} metros é {cm:.2f} centímetros e {mm:.2f} milímetros. ')