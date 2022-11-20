
import turtle
#耳朵
turtle.penup()
turtle.pencolor('pink')
turtle. goto(-10,80)
turtle. pendown()
turtle.dot(40,'pink')
turtle.dot(20,'red')
turtle.penup()
turtle. goto(60,80)
turtle.pendown()
turtle.dot(40,'pink')
turtle.dot(20,'red')
turtle. penup()
turtle.fillcolor('pink')
turtle. home()
turtle.pendown()
turtle.begin_fill()
#脸
for i in range(3):
 turtle.forward(50)
 turtle.circle(30,120)
turtle.end_fill()

#turtle.pencolor('black')
'''
turtle. begin_fill()
turtle.left(90)
turtle. forward(80)

turtle.circle(20)
#turtle.dot(20,'pink')
turtle. right(180)
turtle.goto(50,80)

turtle.circle(20)
turtle.end_fill()
'''

turtle.penup()
turtle.goto(40,60)
turtle.down()
turtle.fillcolor('red')
turtle.begin_fill()
turtle. right(180)
for i in range(3):
 turtle.forward(30)
 turtle.circle(10,120)
turtle.end_fill()
turtle. pencolor('black')
turtle. fillcolor('black')
turtle. penup()
turtle.goto(35,50)
turtle.begin_fill()
turtle.pendown()
turtle.forward(20)
turtle.circle(5,150)
turtle.circle(25,60)

turtle. circle(5,150)
turtle.end_fill()


turtle.fillcolor('pink')
turtle.pencolor('pink')
#肚子
turtle. penup()
turtle.home()
turtle.pendown()
turtle. begin_fill()
turtle.goto(-10,10)
turtle. right(130)
turtle. circle(200,30)
turtle. left(100)
turtle.forward(160)
turtle.left(100)
turtle. circle(200,30)
turtle. home()
turtle.end_fill()


turtle.penup()
turtle.pencolor('red')
turtle. goto(0,-85)
turtle.pendown()
turtle. fillcolor('red')
#肚皮
turtle.begin_fill()
turtle.penup()
turtle.forward(70)


turtle. left(90)
turtle. pendown()
turtle.circle(150,30)
turtle.circle(30,120)
turtle. circle(150,30)
turtle. left(90)
turtle.end_fill()
turtle.hideturtle()

