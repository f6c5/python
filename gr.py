from turtle import *
colors = ["red","pink","yellow","blue", "grey", "white"]
bgcolor("black") #set the background color to black
speed(5000)
for x in range(300):
    pencolor(colors[x%6])
    width(x/100+2)
    forward(x)
    left(75)

hideturtle()

done()
