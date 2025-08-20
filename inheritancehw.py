class fair :
    def __init__(self,name,price,noofpeople):
        self.name = name
        self.price = price
        self.noofpeople = noofpeople
class games(fair):
    pass
x = games("momo","1k",1) 
print(x.name,x.price,x.noofpeople)