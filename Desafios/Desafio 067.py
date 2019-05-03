#tabuada de varios números
#um de cada vez
#o programa para quando o valor for negativo
verdade=False
tab=0
while not verdade:
    print ('-='*10)
    print ('>>>>>>TABUADA<<<<<')
    print ('-='*10)
    print (' ')
    n = (int(input('Número para tabuada: ')))
    for i in range (1,11):
        tab=n*i
        print (f'{n} x {i} = {tab}')
    if n<0:
        break
print ('FIM')