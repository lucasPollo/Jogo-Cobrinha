#Projeto jogo da cobra
import turtle
import time
import random

delay = 0.1

# Pontuações
pontuacao = 0
pontuacaoMaxima = 0

# Set up the screen
janela = turtle.Screen()
janela.title("Jogo da Cobrinha")
janela.bgcolor("#000000")
janela.setup(width=600, height=600)
janela.tracer(0) 
janela.res

# Cobra
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("#40F553")
cobra.penup()
cobra.goto(0,0)
cobra.direction = "stop"

# Maça
maca = turtle.Turtle()
maca.speed(0)
maca.shape("square")
maca.color("red")
maca.penup()
maca.goto(0,100)

segmentos = []

# Escrita
escrita = turtle.Turtle()
escrita.speed(0)
escrita.shape("square")
escrita.color("white")
escrita.penup()
escrita.hideturtle()
escrita.goto(0, 260)
escrita.write("Pontuação: 0  Pontuação Máxima: 0", align="center", font=("Courier", 18, "normal"))

# Funções
def go_up():
    if cobra.direction != "down":
        cobra.direction = "up"

def go_down():
    if cobra.direction != "up":
        cobra.direction = "down"

def go_left():
    if cobra.direction != "right":
        cobra.direction = "left"

def go_right():
    if cobra.direction != "left":
        cobra.direction = "right"

def move():
    if cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)

    if cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)

    if cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)

    if cobra.direction == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)

# binds do teclado
janela.listen()
janela.onkeypress(go_up, "w")
janela.onkeypress(go_down, "s")
janela.onkeypress(go_left, "a")
janela.onkeypress(go_right, "d")

#loop principal
while True:
    janela.update()

    # checa colisao com a borda
    if cobra.xcor()>290 or cobra.xcor()<-290 or cobra.ycor()>290 or cobra.ycor()<-290:
        time.sleep(1)
        cobra.goto(0,0)
        cobra.direction = "stop"

       
        for segmento in segmentos:
            segmento.goto(1000, 1000)
  
        segmentos.clear()

        # reseta pontuação
        pontuacao = 0

    
        delay = 0.1

        escrita.clear()
        escrita.write("Pontuação: {}  Pontuação Máxima: {}".format(pontuacao, pontuacaoMaxima), align="center", font=("Courier", 18, "normal")) 

     
    # checar a colisão
    if cobra.distance(maca) < 20:
        # Move a maça para uma nova direção
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        maca.goto(x,y)

        #novoSegmento = pedaço novo da cobra
        novoSegmento = turtle.Turtle()
        novoSegmento.speed(0)
        novoSegmento.shape("square")
        novoSegmento.color("#40F553")
        novoSegmento.penup()
        segmentos.append(novoSegmento)

        delay -= 0.001

        # Aumenta a  pontuação
        pontuacao += 10

        if pontuacao > pontuacaoMaxima:
            pontuacaoMaxima = pontuacao
        
        escrita.clear()
        escrita.write("Pontuação: {}  Pontuação Máxima: {}".format(pontuacao, pontuacaoMaxima), align="center", font=("Courier", 18, "normal")) 

    
    for index in range(len(segmentos)-1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

   
    if len(segmentos) > 0:
        x = cobra.xcor()
        y = cobra.ycor()
        segmentos[0].goto(x,y)

    move()    

 
    for segmento in segmentos:
        if segmento.distance(cobra) < 20:
            time.sleep(1)
            cobra.goto(0,0)
            cobra.direction = "stop"
        
        
            for segmento in segmentos:
                segmento.goto(1000, 1000)
        
            
            segmentos.clear()

            # reseta a pontuação
            pontuacao = 0

           
            delay = 0.1
        
            # atualiza display pontos
            escrita.clear()
            escrita.write("Pontuação: {}  Pontuação Máxima: {}".format(pontuacao, pontuacaoMaxima), align="center", font=("Courier", 18, "normal"))

    time.sleep(delay)

janela.mainloop()