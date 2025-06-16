import turtle
x = turtle.Screen()
x.bgcolor("light blue")
x.title("spiral")
y=turtle.Turtle()
size=0
while True:
    for i in range (4):
        y.fd(size+1)
        y.left(90)
        size=(size-5)
    size=(size+1)
turtle.done()
