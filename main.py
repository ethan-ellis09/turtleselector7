import turtle
import random
from selectors import (SelectSelector)

screen = turtle.Screen()
screen.screensize(canvwidth=500,canvheight=500)
screen.bgcolor("black")

t=turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write("Background Color",font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write("1. Tan",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('azure')
t.write("2. Azure",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('aquamarine')
t.write("3. AquaMarine",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('DarkKhaki')
t.write("4. DarkKhaki",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write("Select a Color",font=("arial",30,"normal"),align="center")

choose=int(input("Select a color:"))
if choose == 1:
    screen.bgcolor("Tan")
elif choose == 2:
    screen.bgcolor("Azure")
elif choose == 3:
    screen.bgcolor("Aquamarine")
else:
    screen.bgcolor("DarkKhaki")

t.clear()

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('Black')
t.write("Enter your name",font=("arial",30,"normal"),align="center")
t.clear()
name = input("Enter your name: ")
#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
operation = random.randint(1,4)

if operation == 1:
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write('+', font=("arial", 30, "normal"), align="center")
    solution = num1 + num2

elif operation == 2:
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write('-', font=("arial", 30, "normal"), align="center")
    solution = num1 - num2

elif operation == 3:
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write('X', font=("arial", 30, "normal"), align="center")
    solution = num1 * num2

elif operation == 4:
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)
    sign= random.randint(1,2)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write('/', font=("arial", 30, "normal"), align="center")
    if sign==2:
        num2 = -1 * num2
    solution = float(num1 / num2)

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('Blue')
t.write(name,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('green')
t.write(num1,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('HotPink')
t.write(num2,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('black')
t.write('=',font=("arial",30,"normal"),align="center")


ans = float(input("Enter the answer: "))


t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('Red')
t.write(solution,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("Your answer: "+str(ans),font=("arial",30,"normal"),align="center")


if ans == solution:
    screen.bgcolor("DodgerBlue")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("Correct!", font=("arial",30,"normal"),align="center")

else:
    screen.bgcolor('darkOrange')
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("Incorrect!", font=("arial", 30, "normal"), align="center")








t.hideturtle()
turtle.done()