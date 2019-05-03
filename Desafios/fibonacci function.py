def fibo (x):
    if x==1:
        return 0
    if x==2:
        return 1
    return fibo(x-1)+fibo(x-2)


def fibo2 (x):
    result=0
    n1=0
    n2=1
    print('0',end=' => ')
    for i in range(n-1):
        result = n1 + n2
        n2=n1
        n1=result
        if i==n-2:
            print(result)
        else:
            print(result,end=' => ')
    return result

n = int(input('Quantos termos você deseja: '))
(fibo2(n))


