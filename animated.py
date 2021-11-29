import turtle
import os
import random
import time

kray_na_igrata = False
daljina_pole = 37

ekran = turtle.Screen()
ekran.title("Гоненица за Силата е в Теб")
ekran.bgcolor("#DFB9CA")
ekran.setup(width=1200, height=400)
ekran.tracer(0)



# pole
for kletka in range(1, daljina_pole+1):

    # kvadratche
    kvadratche = turtle.Turtle()
    kvadratche.speed(0)
    kvadratche.shape("square")
    kvadratche.shapesize(stretch_wid=1.2,stretch_len=1.2)
    kvadratche.color("#F34616")
    kvadratche.penup()
    kvadratche.goto((kletka * (20+10)) - 580, 0)
# eof kletka

#igrach
pionka = turtle.Turtle()
pionka.pozicia = 0
pionka.speed(0)
pionka.shape("circle")
pionka.color("#18730B")
pionka.penup()
pionka.goto((pionka.pozicia * (20+10)) - 580, 0)


text = turtle.Turtle()
text.speed(0)
text.color("#F34616")
text.penup()
text.hideturtle()
text.goto(0, 20)
text.clear()
text.setheading(180)
text.write("Клавиш i, за да играете", align="center", font=("Courier", 24, "bold"))


# Functions
def roll_dice():
    zar = random.randint(1, 6)
    print(zar)

    text.goto(0, 20)
    text.clear()
    text.write("Падна се: " + str(zar), align="center", font=("Courier", 24, "bold"))

    if pionka.pozicia == 0:
        if zar == 6:
            pionka.pozicia = 1
            zar = 0
            text.sety(text.ycor() - 100)
            text.write("Влизаш!", align="center", font=("Courier", 24, "bold"))
            ekran.update()

    if pionka.pozicia != 0:
        while zar == 6:
            print(" Допълнително Хвърляне! ")
            if pionka.pozicia + zar <= daljina_pole:
                pionka.pozicia = pionka.pozicia + zar
            zar = random.randint(1, 6)
            print("  ", zar)
            text.sety(text.ycor() - 100)
            text.write("допълнително хвърляне: " + str(zar), align="center", font=("Courier", 24, "bold"))
            ekran.update()
        
        if pionka.pozicia + zar <= daljina_pole:
                pionka.pozicia = pionka.pozicia + zar

    
    if pionka.pozicia == daljina_pole:
        global kray_na_igrata
        kray_na_igrata = True
        print("Благодаря за играта.")

# Keyboard bindings
ekran.listen()
ekran.onkeyrelease(roll_dice, "r")
ekran.onkeyrelease(roll_dice, "i") # и на кирилица
ekran.onkeyrelease(roll_dice, "space")
ekran.onkeyrelease(roll_dice, "Return")
ekran.onkeyrelease(roll_dice, "Up")

# Главен цикъл за играта
while True:
    
    if pionka.xcor() < ((pionka.pozicia * (20+10)) - 580):
        if pionka.speed == 0:
            # изчисляваме скоростта s = v.t; v = s/t
            път = ((pionka.pozicia * (20+10)) - 580) - pionka.xcor()
            време = 300
            pionka.speed = път / време
        pionka.forward(pionka.speed)
    else:
        pionka.speed = 0
        
    ekran.update()

    if kray_na_igrata == True and (pionka.xcor() >= ((pionka.pozicia * (20+10)) - 580)):
        
        text.clear()
        text.color("#18730B")
        text.write("Край на Играта :)", align="center", font=("Courier", 24, "bold"))

        ekran.update()
        time.sleep(2)
        break
