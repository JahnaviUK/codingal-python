class vehicle:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
x = vehicle(240,"yellow")
print ("speed = ",x.speed)
print ("color = ",x.color)

class animal:
    def __init__(self,size,color):
        self.size = size
        self.color = color
y = animal("small","brown")
print ("size = ",y.size)
print ("color = ",y.color)
