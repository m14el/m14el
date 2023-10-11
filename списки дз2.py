
a=int(input('введите кол-во элементов:'))
lst=list(map(int,input().split()))
lst.insert(0, lst.pop())
print(lst)