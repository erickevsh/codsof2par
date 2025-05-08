import turtle
import time

class CursorControl:
    wn = None
    space = None
    speed = 1

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(width=1100, height=800)
        self.wn.title('TORTUGA GORDA ^_____^')
        self.wn.bgcolor('White')
        self.space = turtle.Turtle()
        self.space.shape('square')
        self.space.color('red')
        self.space.penup()
    
    def arriba(self):
        self.space.setheading(90)

    def abajo(self):
        self.space.setheading(270)

    def izquierda(self):
        self.space.setheading(180)
    
    def derecha(self):
        self.space.setheading(0)

    def trigger(self):
        self.wn.listen()
        self.wn.onkey(self.arriba, 'Up')
        self.wn.onkey(self.abajo, 'Down')
        self.wn.onkey(self.izquierda, 'Left')
        self.wn.onkey(self.derecha, 'Right')

        while True:
            if self.space.xcor() > 1100 / 2  or self.space.xcor() <- 1100 / 2 or self.space.ycor() > 800 / 2 or self.space.ycor() <- 800 / 2:
                time.sleep(0)
                self.space.goto(0,0)
                self.space.direction = 'stop'
            self.space.forward(self.speed)

c = CursorControl()
c.trigger()