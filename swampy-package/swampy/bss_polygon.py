# Polygon excercise from Week 0
# Name: Sidd Tewari

import math
from TurtleWorld import * 
world = TurtleWorld()
lee = Turtle()
lee.delay = 0.02
print lee

def polygon(Turtle,len,sides):
	world.clear()
	angle = 360.0/sides
	for i in range(sides):
		fd(Turtle,len)
		lt(Turtle,angle)

def circle(Turtle,radius):
	world.clear()
	pi = math.pi
	circum = 2*pi*radius
	length = radius/5		    # hard-coded approximation 
	sides = int(circum/length)  # circum == length * sides
	polygon(Turtle,length,sides)

def arc(Turtle,radius,theta):
	world.clear()
	pi = math.pi
	circum = 2*pi*radius
	length = radius/5		    # hard-coded approximation 
	sides = int(circum/length)  # circum == length * sides
	angle = theta/sides
	for i in range(sides):
		fd(Turtle,length)
		lt(Turtle,angle)

arc(lee,10,360)
arc(lee,30,90)
arc(lee,30,180)

	
polygon(lee,100,3)
polygon(lee,150,4)
polygon(lee,50,5)
polygon(lee,50,6)
polygon(lee,60,8)

circle(lee,23)
circle(lee,50)
circle(lee,100)

wait_for_user()					