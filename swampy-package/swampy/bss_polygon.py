# Polygon excercise from Week 0
# Name: Sidd Tewari

import math
from TurtleWorld import * 

def square(t, length):
	""" Draws a square with sides of the given length
	Returns the turtle to the starting position and location
	This function is better generalized in polygon / draw
	"""
	for i in range(4):
		fd(t, length)
		lt(t)
	# polygon(t, length, 4)
	# draw(t, length, 4, 90)

def polygon(t, sides, length):
	"""Draws a polygon of given sides for given length. Angle is calculated
	- The exterior angles of an n-sided regular polygon are 360/n degrees)
	"""
	angle = 360.0/sides
	draw(t, length, sides, angle)

def circle(t, r):
	"""Draws a circle - which is basically an arc with a theta of 360.0 degrees
	"""
	circumfrence = 2 * math.pi * r
	n = int(circumfrence/3) + 1
	length = circumfrence / n
	polygon(t, n, length)

	# length, sides = circularCalculations(radius)
	# angle = 360.0/sides
	# draw(t, length, sides, angle)
	
	# arc(t, r, 360.0)

def arc(t, radius, theta):
	# arc takes an additional parameter of theta
	""" Draws an arc with the given radius and theta
	"""
	# take the function arguments provided and pass them as parameter for 
	# the calculations function
	length, sides = circularCalculations(radius)
	angle = theta/sides
	draw(t, length, sides, angle)

def circularCalculations(r):
	# this function is called by both circle and ar for calculations
	circum = 2*math.pi*r
	length = r/5		    # hard-coded approximation 
	sides = int(circum/length)  # circum == length * sides
	return (length, sides)

def draw(t, length, sides, angle):
	#My function - equivalent to polyline in Ch-4; docstring from book
	"""Draws n (== sides) line segments with the given length and angle 
	(in degrees) between them. t is a Turtle.
	"""
	for i in range(sides):
		fd(t, length)
		lt(t, angle)

def setup():
	# clear TurtleWorld canvas before each test is run
	world.clear()

def move(t,length):
	"""Move Turtle(t) forward (length) units without leaving a trace. 
	Leaves the pen down after moving.
	"""
	pu(t)
	fd(t, length)
	pd(t)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
	world = TurtleWorld()

	lee = Turtle()
	lee.delay = 0.001

	# These are tests to check for drawing arcs, circle, & polygons. 
	# arc(lee,10,360)
	# arc(lee,30,180)
	setup()
	arc(lee,10,50)
	
	setup()
	polygon(lee, 3, 50)
	move (lee, 5)
	polygon(lee, 8, 60)
	move (lee, 5)
	polygon(lee, 4, 15)
	polygon(lee, 5, 40)
	polygon(lee, 6, 20)
	
	setup()
	# circle(lee,23)
	# circle(lee,50)
	circle(lee,80)
	#petal(lee, 60.0, 60.0)
	wait_for_user()					