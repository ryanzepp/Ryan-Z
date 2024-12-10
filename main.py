import turtle


t = turtle.Turtle()
t2 = turtle.Turtle()
t2.penup()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1000,1000)
t.hideturtle()
x = 1
screen.bgcolor("medium blue")
t.color("white")
t.penup()
t.goto(0,75)
t.pendown()
t.write("All About Me", font=("Arial", 65, "bold"), align="center")
t.penup()
t.goto(0,0)
t.pendown()
t.write("By Ryan Zeppuhar", font=("Arial", 24, "bold"), align="center")
t.penup()
t.goto(0,-20)
t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
t.pendown()


enter = input("Press enter to continue: ")
screen.bgcolor("lightgreen")



t.clear()
t.penup()

t.color("HotPink")
t.pencolor("Pink")
t.setheading(0)

t.goto(100,-200)
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()
t.goto(0,100)



t.write("These are my Favorite Foods!", font=("Arial", 50, "bold"), align="center")
t.penup()
t.goto(0, 0)
t.pendown()
turtle.addshape("food1.gif")
t2.shape("food1.gif")
a = t2.stamp()
t2.goto(-100,-100)
turtle.addshape("pizza.gif")
t2.shape("pizza.gif")
b = t2.stamp()
t2.goto(200,200)
turtle.addshape("egg.gif")
t2.shape("egg.gif")
c = t2.stamp()

enter = input("Press enter to continue: ")
screen.bgcolor("lightgreen")
t.clear()
t2.hideturtle()
t2.clear()
t.penup()
t.goto(0, 300)

t.goto(0, 300)
t.pendown()
t.write("These are my Favorite Hobbies!", font=("Arial", 50, "bold"), align="center")
t.penup()
t.goto(100, 100)
t.pendown()
turtle.addshape("hockey.gif")
t2.shape("hockey.gif")
a = t2.stamp()
t2.goto(0,0)
turtle.addshape("hunting.gif")
t2.shape("hunting.gif")
a = t2.stamp()
t2.goto(-100,-100)
turtle.addshape("fishing.gif")
t2.shape("fishing.gif")
a = t2.stamp()
t2.goto(-200,-200)
turtle.addshape("track.gif")
t2.shape("track.gif")
a = t2.stamp()
t2.goto(-250,-250)



enter = input("Press enter to continue: ")
screen.bgcolor("pink")
t.clear()
t2.clear()
t.penup()
t.goto(0, 300)
t.write("This is My Favorite Movie!", font=("Arial", 50, "bold"), align="center")
t.penup()
t.goto(100, 100)
t.pendown()
turtle.addshape("movie.gif")
t2.shape("movie.gif")
a = t2.stamp()
t2.goto(100,100)





enter = input("Press enter to continue: ")

screen.bgcolor("purple")
t2.clear()
t.clear()
t.penup()
t.goto(0, 300)
t.write("This is My Favorite sport!", font=("Arial", 50, "bold"), align="center")
t.penup()
t.goto(100, 100)
t.pendown()
turtle.addshape("hockey.gif")
t2.shape("hockey.gif")
a = t2.stamp()
t2.goto(0,0)





enter = input("Press enter to continue: ")
screen.bgcolor("red")
t.clear()
t.penup()
t.goto(0, 300)



turtle.done()










