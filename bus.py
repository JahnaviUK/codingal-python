class vehicle :
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehicle):
    pass
x = bus("school volvo",180,12) 
print(x.name,x.max_speed,x.mileage)
