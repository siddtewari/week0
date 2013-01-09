# Polygon excercise from Week 0

# Name: Sidd Tewari

import math
from TurtleWorld import * 
world = TurtleWorld()			
lee = Turtle()				
print lee

def polygon(Turtle,len,n):
	angle = 360.0/n
	for i in range(n):
		fd(Turtle,len)
		lt(Turtle,angle)

def circle(t,r):
	world.clear()
	pi = math.pi
	circum = 2*pi*r
	length = r/5 		        # hard coded approximation for length
	sides = int(circum/length)  # circum == length * sides
	polygon(lee,length,sides)
	
circle(lee,23)
circle(lee,50)
cirle(lee,500)
wait_for_user()					
