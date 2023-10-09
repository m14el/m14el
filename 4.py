import math
running=True
while running:
    a=int(input('введите 5-ти значное число:'))
    if a>10000 and a<99999:
        b=list(str(a))
        c=(int(b[3]) ** int(b[4])) * int(b[2]) / (int(b[0]) - int(b[1]))
        print(c)
        running=False
print('end')



