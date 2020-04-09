import turtle
import time
import random

#Variables
posponer = 0.15
puntos = 0
dirInicial = "stop"

#Configuracion de la ventana
wn = turtle.Screen()    # establecer wn al objeto de la ventana
width = 600
height = 600
wn.setup(width, height)      # establecer el tamaño de la ventana de 800 por 600 píxeles
wn.bgcolor("Dark Slate Gray")     # establecer el color de fondo de la ventana
wn.title("Snake - Puntos: " + str(puntos))       # establecer el título de la ventana
wn.tracer(0)

#Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("Yellow Green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("Orange Red")
comida.penup()
comida.goto(0,100)

#Segmentos
segmentos = []

#Dibujar cuadricula
def cuadricula():
    grid = turtle.Turtle()
    grid.hideturtle()
    grid.color("gray")
    grid.speed(0)

    x0 = int(- (width / 2))
    y0 = int(- (height / 2))
    grid.penup()

    for xPos in range(x0 + 10, width, 20):
        for yPos in range(y0, height, 20):
            grid.setpos(xPos, yPos)
            grid.pendown()
        grid.penup()
    
    for yPos in range(y0 + 10, height, 20):
        for xPos in range(x0, width, 20):
            grid.setpos(xPos, yPos)
            grid.pendown()
        grid.penup()

cuadricula()

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 0)

def arriba():
    global dirInicial
    if len(segmentos) == 0 or (len(segmentos) > 0 and dirInicial != "down"):
        cabeza.direction = "up"

def abajo():
    global dirInicial
    if len(segmentos) == 0 or (len(segmentos) > 0 and dirInicial != "up"):
        cabeza.direction = "down"

def izquierda():
    global dirInicial
    if len(segmentos) == 0 or (len(segmentos) > 0 and dirInicial != "right"):
        cabeza.direction = "left"

def derecha():
    global dirInicial
    if len(segmentos) == 0 or (len(segmentos) > 0 and dirInicial != "left"):
        cabeza.direction = "right"

#Funciones
def mov():
    global dirInicial
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        dirInicial = "up"

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        dirInicial = "down"

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        dirInicial = "right"

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)   
        dirInicial = "left" 

def reset():
    texto.clear()
    texto.write("Game Over", align="center", font=("Courier", 35, "normal"))
    time.sleep(1)
    texto.clear()
    cabeza.goto(0, 0)
    cabeza.direction = "stop"
    puntos = 0
    wn.title("Snake - Puntos: " + str(puntos))
    global posponer
    posponer = 0.15

    for index in range(len(segmentos) - 1, -1, -1):
        segmentos[index - 1].clear()
        #Hide the turtle
        segmentos[index - 1].ht()
        del segmentos[index - 1]

def aparecerComida():
    x = random.randint(-290, 270)
    while x%20 != 0:
        x = x + 1

    y = random.randint(-290, 270)
    while y%20 != 0:
        y = y + 1

    comida.goto(x,y)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        reset()

    #Colision con la comida
    if cabeza.distance(comida) < 20:
        puntos = puntos + 10
        if puntos%100 == 0:
            posponer = posponer - 0.01
        aparecerComida()

        wn.title("Snake - Puntos: " + str(puntos))

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("Medium Sea Green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
    
    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)
    
    mov()

    #Colision con el cuerpo
    for seg in segmentos:
        if seg.distance(cabeza) < 20:
            reset()
    
    #Colision comida con el cuerpo
    for seg in segmentos:
        if seg.distance(comida) < 20:
            aparecerComida()

    time.sleep(posponer)
    
wn.exitonclick()