num=int(input())
if num>0 and num%2==0:
    print('положительное чётное число')
elif num<0 and num%2!=0:
    print('отрицательное  нечётное число')
elif num==0:
    print('нулевое число')
elif num%2==0 and num<0:
    print('чётное отрицательное число')
elif num%2!=0 and num>0:
    print('нечётное положительное число')
print('конец')