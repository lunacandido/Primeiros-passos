### turtle Olá, tartaruguinhas 
import turtle            # permite usar as funções e objetos do módulo turtle
wn = turtle.Screen()     # cria uma janela gráfica
wn.bgcolor("black") # define a cor de fundo da janela

luna = turtle.Turtle()   # cria um turtle chamado luna
luna.pensize(15)        #espessura da caneta
luna.color("red")       #cor da tartaruga 

for i in range(12):
    luna.forward(100)        # manda o alex se mover 100 unidades para frente
    luna.left(30)            # roda de 30 graus para a esquerda
    luna.forward(30)         # desenha 30 unidades
luna.goto(0,0)               # orientação da tartaruga
wn.exitonclick()