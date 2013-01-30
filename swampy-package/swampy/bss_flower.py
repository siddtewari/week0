# Flower excercise (4.2) from Week 0
# Name: Sidd Tewari

import math

from TurtleWorld import * 		
world = TurtleWorld()		
world.clear()	
lee = Turtle()				
lee.delay = 0.01
print lee

from bss_polygon import *

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
	for i in range(sides):
		fd(Turtle,length)
		lt(Turtle,angle)

def flower(Turtle,length,theta):
	for i in range(2):
		arc(lee,50,100)
		lt(lee,	)

wait_for_user()					

