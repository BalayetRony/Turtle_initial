import turtle 
from numpy.random import uniform

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('yellow')
turtle.speed(0)           #turtle speed line
turtle.penup()
turtle.goto(-500, 140)

for i in range(50):                   #Line range
    turtle.write(i, align="center")
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.backward(310)
    turtle.left(90)
    turtle.forward(20)
    
turtle.speed(0)

turtle1 = turtle.Turtle()   #Red turtle description
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-500, 100)
turtle1.pendown()

turtle2 = turtle.Turtle()   #Blue turtle description
turtle2.color("blue")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-500, 60)
turtle2.pendown()

turtle3 = turtle.Turtle()   #Green turtle description
turtle3.color("green")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-500, 20)
turtle3.pendown()

turtle4 = turtle.Turtle()   #cyan turtle description
turtle4.color("cyan")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-500, -20)
turtle4.pendown()

turtle5 = turtle.Turtle()       #Black turtle description
turtle5.color("black")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-500, -60)
turtle5.pendown()

flag = 1

while flag == 1:
    PlayAgain = input("Wanna Play again?(y/n) ")
    
    if PlayAgain == "y":
        
        turtle1.goto(-500, 100)
        turtle2.goto(-500, 60)
        turtle3.goto(-500, 20)
        turtle4.goto(-500, -20)
        turtle5.goto(-500, -60)
        
        turtle1.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        
        for i in range(340):
        
            if turtle1.xcor() < 480:
                turtle1.forward(uniform(3, 15))
            else:
                print('Red Turtle has won')
                print('Game Over')
                break
        
            if turtle2.xcor() < 480:
                turtle2.forward(uniform(3, 15))
            else:
                print('Blue Turtle has won')
                print('Game Over')
                break
        
            if turtle3.xcor() < 480:
                turtle3.forward(uniform(3, 15))
            else:
                print('Green Turtle has won')
                print('Game Over')
                break
        
            if turtle4.xcor() < 480:
                turtle4.forward(uniform(3, 15))
            else:
                print('Cyan Turtle has won')
                print('Game Over')
                break
        
            if turtle5.xcor() < 480:
                turtle5.forward(uniform(3, 15))
            else:
                print('Black Turtle has won')
                print('Game Over')
                break
    else:
        turtle.Screen().bye()

wn.exitonclick()
turtle.done()
