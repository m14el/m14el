n=int(input('введите кол-во элементов:'))
for i in range(n):
    spisok=list(map(int,input().split()))
    e=set(spisok)
    print(len(e))
