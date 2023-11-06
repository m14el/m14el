class Transport:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage


class Autobus(Transport):
    def avtik(self,name,max_speed,mileage):
        name=input('enter the name of bus: ')
        max_speed=int(input('enter the max speed of bus: '))
        mileage=int(input('enter the mileage of bus: '))
        print(f'Это автобус марки {name}, который развивает максимальную скорость в '
              f'{max_speed} км/ч и пробег у него {mileage} км')

autobus=Autobus(name='',max_speed='',mileage='')
autobus.avtik(name='',max_speed='',mileage='')
