import turtle
import random
import time

delay = 0.1
distancia = 15
puntuación = 0
récord = 0
segmentos = []

def juego():

    wn = turtle.Screen()
    wn.title('serpiente')
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # creación de la serpiente
    jugador = turtle.Turtle()
    jugador.speed(0)
    jugador.penup()
    jugador.shape('square')
    jugador.color('black')
    jugador.direccion = 'stop'

    #puntos
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(0, 250)
    pen.hideturtle()
    pen.write('puntuación: {}  récord: {}'.format(puntuación, récord), align='center', font=('century gothic', 25))

    # aparición de los puntos
    punto = turtle.Turtle()
    punto.shape('circle')
    punto.color('red')
    punto.speed(0)
    punto.penup()
    punto.goto(-50, 100)


    # funciones
    def movimiento():
        if jugador.direccion == 'up':
            jugador.sety(jugador.ycor() + distancia)
        if jugador.direccion == 'down':
            jugador.sety(jugador.ycor() - distancia)
        if jugador.direccion == 'left':
            jugador.setx(jugador.xcor() - distancia)
        if jugador.direccion == 'right':
            jugador.setx(jugador.xcor() + distancia)

    def arriba():
        if jugador.direccion != 'down':
            jugador.direccion = 'up'

    def abajo():
        if jugador.direccion != 'up':
            jugador.direccion = 'down'

    def izquierda():
        if jugador.direccion != 'right':
            jugador.direccion = 'left'

    def derecha():
        if jugador.direccion != 'left':
            jugador.direccion = 'right'

    # controlar la serpiente
    wn.listen()
    wn.onkey(arriba, 'Up')
    wn.onkey(abajo, 'Down')
    wn.onkey(izquierda, 'Left')
    wn.onkey(derecha, 'Right')


    def perder():
        global puntuación
        global récord
        pen.clear()
        if puntuación > récord:
            récord = puntuación
        puntuación = 0
        pen.write('puntuación: {}  récord: {}'.format(puntuación, récord), align='center', font=('century gothic', 25))
        jugador.goto(0, 0)
        time.sleep(0.5)
        jugador.direccion = 'stop'
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        segmentos.clear()


    def moverpunto():
        if jugador.distance(punto) < 20:
            # mover el punto
            y = random.randint(-280, 280)
            x = random.randint(-280, 280)
            punto.goto(x, y)
            # subir puntuación
            global puntuación
            puntuación += 1
            pen.clear()
            pen.write('puntuación: {}  récord: {}'.format(puntuación, récord), align='center', font=('century gothic', 25))
            # alargar cola
            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.penup()
            nuevo_segmento.shape('square')
            nuevo_segmento.color('grey')
            segmentos.append(nuevo_segmento)
        # hacer avanzar la cola
        for i in range(len(segmentos)-1, 0, -1):
            x = segmentos[i - 1].xcor()
            y = segmentos[i - 1].ycor()
            segmentos[i].goto(x, y)
        # pegar cola a la cabeza
        if len(segmentos) > 0:
            x = jugador.xcor()
            y = jugador.ycor()
            segmentos[0].goto(x, y)

    while True:
        wn.update()
        moverpunto()
        movimiento()
        # Salirse de los bordes
        if jugador.xcor() > 290 or jugador.xcor() < -290 or jugador.ycor() > 290 or jugador.ycor() < -290:
            perder()
        #chocar con la cola
        for segmento in segmentos:
            if segmento.distance(jugador) < distancia:
                perder()
        time.sleep(delay)
