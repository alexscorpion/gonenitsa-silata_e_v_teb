import turtle
import os

wn = turtle.Screen()
wn.title("Гоненица")
wn.bgcolor("#DFB9CA")
wn.setup(width=1200, height=400)
wn.tracer(0)



# pole
for kletka in range(1, 38):

    # kvadratche
    kvadratche = turtle.Turtle()
    kvadratche.speed(0)
    kvadratche.shape("square")
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
text.write("Roll: 6", align="center", font=("Courier", 24, "bold"))


# Functions
def roll_dice():
    igrach.pozicia_na_igrach += 2
    igrach.setx((igrach.pozicia_na_igrach * (20+10)) - 580)


# Keyboard bindings
wn.listen()
wn.onkeypress(roll_dice, "r")
wn.onkeypress(roll_dice, "space")
wn.onkeypress(roll_dice, "Up")

# Main game loop
while True:
    wn.update()
