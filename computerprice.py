class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling price{}".format (self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price
keyboard = computer()
keyboard.sell()
keyboard.setmaxprice(320)
keyboard.sell()