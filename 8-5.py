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
                self.space = turtle.Turtle()
        self.space.shape('square')
        self.space.color('red')
        self.space.penup()

        # AGREGAR 3 CUADRADOS
        self.cuadrados = []
        posiciones = [(-200, 200), (0, -150), (200, 100)]
        for pos in posiciones:
            cuadrado = turtle.Turtle()
            cuadrado.shape('square')
            cuadrado.color('blue')
            cuadrado.penup()
            cuadrado.goto(pos)
            self.cuadrados.append(cuadrado)
                def detectar_colision(self):
                
         for cuadrado in self.cuadrados:
            if self.space.distance(cuadrado) < 20:
                print("¡Colisión con un cuadrado!")


    
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
        self.space.forward(self.speed)
        self.detectar_colision()



        while True:
            if self.space.xcor() > 1100 / 2  or self.space.xcor() <- 1100 / 2 or self.space.ycor() > 800 / 2 or self.space.ycor() <- 800 / 2:
                time.sleep(0)
                self.space.goto(0,0)
                self.space.direction = 'stop'
            self.space.forward(self.speed)

c = CursorControl()
c.trigger()
            time.sleep(0.01)
