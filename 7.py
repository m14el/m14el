Mike=float(input())
Ivan=float(input())
invest=float(input())
if (Mike>=invest) and (Ivan>=invest):
    print(2)
elif ((Mike>=invest) and Ivan<=invest):
    print('Mike')
elif ((Ivan>=invest))and Mike<=invest:
    print('Ivan')
elif ((Mike+Ivan)>=invest):
    print(1)
elif (Mike+Ivan)<=invest:
    print(0)