def factorial(number):
    if number==0:
        return 1
    return factorial(number-1)*number

list=[]
y=int(input('enter number: '))
for i in range(y,0,-1):
    print(factorial(i))



