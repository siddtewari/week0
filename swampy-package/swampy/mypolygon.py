from TurtleWorld import *  #imports everything from the TurtleWorld module (of the swampy package)

world = TurtleWorld() #creates a TurtleWorld assigned to world
bob = Turtle() #creates a Turtle assigned to bob
print bob

def reposition(Turtle,n):
	pu(bob)
	rt(bob)
	fd(bob,n)
	lt(bob)
	pd(bob)

for i in range(4):
	print 'Hello!'

reposition(bob,100)

for i in range(4):
	fd(bob,100)
	lt(bob)

wait_for_user()