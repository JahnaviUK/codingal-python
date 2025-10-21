class Ferrari ():
    def speed(self):
        print("Ferrari goes 350 km/h")
    def race(self):
        print("Ferrari dominates F1 with its red speed machine!")
    def  sound (self):
        print( "Vroom! A loud F1 roar!")
class BMW ():
    def speed(self):
        print("BMW goes 250 km/h")
    def race(self):
        print("BMW focuses on endurance races, not F1 anymore.")
    def  sound (self):
        print("Smooth and quiet luxury engine sound.")
i = Ferrari()
u = BMW()
for car in(i,u):
    car.speed()
    car.race()
    car.sound() 