# Polygon excercise from Week 0
# Name: Sidd Tewari

import math
from TurtleWorld import * 
world = TurtleWorld()
lee = Turtle()
lee.delay = 0.02
print lee

def polygon(Turtle,length,sides):
	angle = 360.0/sides
	draw(Turtle,length,sides,angle)

def circle(Turtle,radius):
	length, sides = circularCalculations(Turtle,radius)
	angle = 360.0/sides
	draw(Turtle,length,sides,angle)

def arc(Turtle,radius,theta):
	length, sides = circularCalculations(Turtle,radius)
	angle = theta/sides
	draw(Turtle,length,sides,angle)

def circularCalculations(Turtle,radius):
	pi = math.pi
	circum = 2*pi*radius
	length = radius/5		    # hard-coded approximation 
	sides = int(circum/length)  # circum == length * sides
	return (length,sides)

def draw(Turtle,length,sides,angle):
	world.clear()
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