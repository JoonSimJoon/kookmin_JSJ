import time
from turtle import *
pensize(10)
penup()
goto(0,100)
setheading(0)
pendown()
circle(100)

penup()
goto(0,140)
pendown()
circle(60,70)

penup()
goto(0,140)
setheading(360)
pendown()
circle(60,-70)

penup()
goto(30,240)
pendown()
dot(20)

penup()
goto(-30,240)
pendown()
dot(20)

penup()
goto(0,-100)
s = "학번: 20223100\n 이름: 심준"
write(s, align="center",font=("",20))
time.sleep(3)