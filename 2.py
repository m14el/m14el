lst=['dryopithecus','australopithecus','homo erectus','homo sapiens','homo sapiens sapiens']
a1=str(input('1-ый этап развитя человека:'))
a2=str(input('2-ой этап развитя человека:'))
a3=str(input('3-ий этап развитя человека:'))
a4=str(input('4-ый этап развитя человека:'))
a5=str(input('5-ый этап развитя человека:'))

if a1==lst[0] and a2==lst[1] and a3==lst[2] and a4==lst[3] and a5==lst[4]:
    print('верно')
    print(a1,a2,a3,a4,a5,sep='=>')
else:
    print('не верно')


