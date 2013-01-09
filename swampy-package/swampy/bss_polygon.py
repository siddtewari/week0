# Polygon excercise from Week 0
# Name: Sidd Tewari

import math
from TurtleWorld import * 
world = TurtleWorld()			

lee = Turtle()
lee.delay = 0.02			
print lee

def setup(Turtle):
	world.clear()
	# pu(Turtle)
	# rt(Turtle)
	# fd(Turtle,100)
	# rt(Turtle)
	# pd(Turtle)


def polygon(Turtle,len,n):
	setup(Turtle)
	angle = 360.0/n
	for i in range(n):
		fd(Turtle,len)
		lt(Turtle,angle)

def circle(t,r):
	pi = math.pi
	circum = 2*pi*r
	length = r/5		        # hard-coded approximation 
	sides = int(circum/length)  # circum == length * sides
	polygon(t,length,sides)
	
polygon(lee,100,3)
polygon(lee,150,4)
polygon(lee,50,5)
polygon(lee,50,6)
polygon(lee,60,8)

#polygon(lee,50,13)

circle(lee,23)
circle(lee,50)
circle(lee,100)
#circle(lee,200)
#circle(lee,1000)
#circle(lee,5000)
wait_for_user()					