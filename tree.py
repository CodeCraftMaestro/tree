from turtle import *
from shape import *
from random import randint
#set the background color
bgcolor("black")

y = -100
width = 240

draw_rectangle(turtle,"brown",-15,y-40,30,40)
#draw rectangle is a fun() which is define in shape file

while width>20:
    width = width-randint(20,30)
    height = randint(15,35)
    x = 0-width/2
    draw_rectangle(turtle,"green",x,y,width,height)
    y = y+height

#draw star

draw_star(turtle,"yellow",4,y,20)
penup()
color("red")
goto(-100,-180)
write("MARRY CHRISTMAS",move = False,font=('Arial',20,'bold'))
hideturtle()
