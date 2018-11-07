#Turtle Racing game.
#Rule 1: press "y" to start race.
#Rule 2: after game over press "y" to play again
#Rule 3: after game over press "n" to exit
""" Have Fun """

import turtle
from numpy.random import uniform

WN = turtle.Screen()       # 2.  Create a screen
WN.bgcolor('yellow')
TURTLE = turtle.Turtle()
TURTLE.speed(0)           #turtle speed line
TURTLE.penup()
TURTLE.goto(-500, 140)

for i in range(50):                   #Line range
    TURTLE.write(i, align="center")
    TURTLE.right(90)
    TURTLE.forward(10)
    TURTLE.pendown()
    TURTLE.forward(300)
    TURTLE.penup()
    TURTLE.backward(310)
    TURTLE.left(90)
    TURTLE.forward(20)

TURTLE.speed(0)

TURTLE1 = turtle.Turtle()   #Red turtle description
TURTLE1.color("red")
TURTLE1.shape("turtle")
TURTLE1.penup()
TURTLE1.goto(-500, 100)
TURTLE1.pendown()

TURTLE2 = turtle.Turtle()   #Blue turtle description
TURTLE2.color("blue")
TURTLE2.shape("turtle")
TURTLE2.penup()
TURTLE2.goto(-500, 60)
TURTLE2.pendown()

TURTLE3 = turtle.Turtle()   #Green turtle description
TURTLE3.color("green")
TURTLE3.shape("turtle")
TURTLE3.penup()
TURTLE3.goto(-500, 20)
TURTLE3.pendown()

TURTLE4 = turtle.Turtle()   #cyan turtle description
TURTLE4.color("cyan")
TURTLE4.shape("turtle")
TURTLE4.penup()
TURTLE4.goto(-500, -20)
TURTLE4.pendown()

TURTLE5 = turtle.Turtle()       #Black turtle description
TURTLE5.color("black")
TURTLE5.shape("turtle")
TURTLE5.penup()
TURTLE5.goto(-500, -60)
TURTLE5.pendown()

FLAG = 1

while FLAG == 1:
    PLAYAGAIN = input("Wanna Play again?(y/n) ")

    if PLAYAGAIN == "y":

        TURTLE1.goto(-500, 100)
        TURTLE2.goto(-500, 60)
        TURTLE3.goto(-500, 20)
        TURTLE4.goto(-500, -20)
        TURTLE5.goto(-500, -60)

        TURTLE1.clear()
        TURTLE2.clear()
        TURTLE3.clear()
        TURTLE4.clear()
        TURTLE5.clear()

        for i in range(340):

            if TURTLE1.xcor() < 465:
                TURTLE1.forward(uniform(3, 15))
            else:
                print('Red Turtle has won')
                print('Game Over')
                break

            if TURTLE2.xcor() < 465:
                TURTLE2.forward(uniform(3, 15))
            else:
                print('Blue Turtle has won')
                print('Game Over')
                break

            if TURTLE3.xcor() < 465:
                TURTLE3.forward(uniform(3, 15))
            else:
                print('Green Turtle has won')
                print('Game Over')
                break

            if TURTLE4.xcor() < 465:
                TURTLE4.forward(uniform(3, 15))
            else:
                print('Cyan Turtle has won')
                print('Game Over')
                break

            if TURTLE5.xcor() < 465:
                TURTLE5.forward(uniform(3, 15))
            else:
                print('Black Turtle has won')
                print('Game Over')
                break
    elif PLAYAGAIN == "n":
        turtle.Screen().bye()

#WN.exitonclick()
#turtle.done()
