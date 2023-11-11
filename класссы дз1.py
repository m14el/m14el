class Cassa:
    total_money=25000
    def top_up(self,add):
        self.add=add
        add+=Cassa.total_money
        return f'в кассе {add}'
    def count_1000(self):
        print(Cassa.total_money//1000)

    def take_away(self,x):
        if x<=self.total_money:
            self.total_money-=x
        else: return f'в кассе не достаточно денег'



cassa=Cassa()
print(cassa.take_away(25200))