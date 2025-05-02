import turtle
class TurtleforNoobs:

    def cuadrado(self):
        skk=turtle.Turtle()
        for i in range(4):
            skk.forward(50)
            skk.right(90)
        turtle.done()

    def estrella(self):
        star=turtle.Turtle()
        star.right(75)
        star.forward(100)
        for i in range(4):
            star.right(144)
            star.forward(100)
        turtle.done()

t=TurtleforNoobs()
t.estrella()