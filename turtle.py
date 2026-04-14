import turtle 
import random
t=turtle.Turtle()
colors= ["red","green","yellow","blue","orange","pink","purple"]
def draw_star(turtle_obj,size ,color ,x ,y):
	turtle_obj.penup()
	turtle_obj.goto(x,y)
	turtle_obj.pendown()
	turtle_obj.color(color)
	for i in range(5):
		turtle_obj.forward(size)
		turtle_obj.right(144)

for i in range(20):
	x=random.randint(-300,300)
	y=random.randint(-300,300)
	color=random.choice(colors)
	size=random.randint(50,180)
    draw_star(turtle_obj: ,size ,color ,x ,y)
    
 
turtle.done()