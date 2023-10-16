s1=input().split()
s2=set()
for i in s1:
    if i in s2:
        print("yes")
    else:
        print("no")
    s2.add(i)