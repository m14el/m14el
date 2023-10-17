pets={}
pets2={}
while (True):
    a=input('введите кличку питомца:')
    if a=='':
        break
    else:
        a1=input('ведите вид питомца:')
        a2=int(input('введите возраст питомца:'))
    age=''
    if a2 %10==1 and a2!=11 and a2%100!=11:
        age='год'
    elif 1<a2%10<=4 and a2//10<4 and a2!=12 and a2!=13 and a2!=14:
        age='года'
    else:
        age='лет'
    a3=input('введите имя владельца:')
    pets2={'вид питомца:':a1,'возраст питомца:':a2,'имя владельца:':a3}
    pets[a]=pets2
    for key in pets.keys():
        print('это',pets2['вид питомца:'],'по кличке:',key,' возраст питомца:',pets2['возраст питомца:'],
              age,'имя владельца:',pets2['имя владельца:'])
    break

