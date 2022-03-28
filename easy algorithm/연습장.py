import turtle

swidth, sheight = 600, 400

turtle.title('무기개색 원그리기')
turtle.ht()
turtle.speed(10)

turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(swidth/2 , -sheight/2)
turtle.pendown()
turtle.goto(swidth/2, sheight/2)
turtle.goto(-swidth/2, sheight/2)
turtle.goto(-swidth/2, -sheight/2)
turtle.goto(swidth/2, -sheight/2)

turtle.penup()
turtle.goto(0, -75)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()
turtle.done()
