# Flower excercise (4.2) from Week 0
# Name: Sidd Tewari

from TurtleWorld import * 		
from bss_polygon import *

def petal(t,r,angle):
	"""Draws a petal using two arcs

	t: TurtleWorld
	r: radius
	angle: angle (degrees) that subtends the arcs
	"""
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def flower(t,n,r,angle):
	"""Draws a flower with n petals.

	t: Turtle
	n: number of petals
	r: radius of the arcs
	angle: angle (degrees) that subtends the arcs
	"""
	for i in range(n):
		petal(t,r,angle)
		lt(t, 360.0/n)

def move(t,length):
	"""Move Turtle(t) forward (length) units without leaving a trace. 
	Leaves the pen down after moving.
	"""
	pu(t)
	fd(t, length)
	pd(t)


world = TurtleWorld()
lee = Turtle()
lee.delay = 0.0001

#petal(lee, 60, 60.0)

move(lee,-100)
flower(lee, 7, 6.0, 60.0)

move(lee,100)
flower(lee, 10, 4.0, 80.0)

move(lee,180)
flower(lee, 20, 14.0, 20.0)

die(lee)

#dump the contents of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()			


# if __name__ == '__main__':
# 	world = TurtleWorld()
# 	bob = Turtle()
# 	bob.delay = 0.01

# 	petal (bob, 100, 15)

# 	wait_for_user()					