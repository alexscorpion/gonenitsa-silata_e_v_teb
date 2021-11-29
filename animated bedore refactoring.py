import turtle
import os
import random
import time

gameOver = False
daljina_pole = 37

screen = turtle.Screen()
screen.title("Гоненица")
screen.bgcolor("#DFB9CA")
screen.setup(width=1200, height=400)
screen.tracer(0)



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
igrach = turtle.Turtle()
igrach.pozicia_na_igrach = 0
igrach.speed(0)
igrach.shape("circle")
igrach.color("#18730B")
igrach.penup()
igrach.goto((igrach.pozicia_na_igrach * (20+10)) - 580, 0)


text = turtle.Turtle()
text.speed(0)
text.color("#F34616")
text.penup()
text.hideturtle()
text.goto(0, 20)
text.clear()
text.setheading(180)
text.write("Press R to Roll", align="center", font=("Courier", 24, "bold"))


# Functions
def roll_dice():
    zar = random.randint(1, 6)
    print(zar)

    text.goto(0, 20)
    text.clear()
    text.write("Roll: " + str(zar), align="center", font=("Courier", 24, "bold"))

    if igrach.pozicia_na_igrach == 0:
        if zar == 6:
            igrach.pozicia_na_igrach = 1
            zar = 0

    if igrach.pozicia_na_igrach != 0:
        while zar == 6:
            print(" Допълнително Хвърляне! ")
            if igrach.pozicia_na_igrach + zar <= daljina_pole:
                igrach.pozicia_na_igrach = igrach.pozicia_na_igrach + zar
            zar = random.randint(1, 6)
            print("  ", zar)
            text.sety(text.ycor() - 100)
            text.write("extra roll: " + str(zar), align="center", font=("Courier", 24, "bold"))
            screen.update()
        
        if igrach.pozicia_na_igrach + zar <= daljina_pole:
                igrach.pozicia_na_igrach = igrach.pozicia_na_igrach + zar

    
    if igrach.pozicia_na_igrach == daljina_pole:
        global gameOver
        gameOver = True
        print("thats all folks")

# Keyboard bindings
screen.listen()
screen.onkeyrelease(roll_dice, "r")
screen.onkeyrelease(roll_dice, "space")
screen.onkeyrelease(roll_dice, "Up")

# Main game loop
while True:
    # https://wecode24.com/stories/abraham/animation-with-turtle-graphics
    
    if igrach.xcor() < ((igrach.pozicia_na_igrach * (20+10)) - 580):
        if igrach.speed == 0:
            # calculate speed s = v.t; v = s/t
            distance = ((igrach.pozicia_na_igrach * (20+10)) - 580) - igrach.xcor()
            _time = 200
            igrach.speed = distance / _time
        igrach.forward(igrach.speed)
    else:
        igrach.speed = 0
        
    screen.update()

    if gameOver == True and (igrach.xcor() >= ((igrach.pozicia_na_igrach * (20+10)) - 580)):
        
        text.clear()
        text.color("#18730B")
        text.write("Game Over :)", align="center", font=("Courier", 24, "bold"))

        screen.update()
        time.sleep(2)
        break
