# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 

world = TurtleWorld()			
lee = Turtle()				
print lee

# This is where you put code to move bob or lee :)

def polygon(Turtle,len,n):
	# to keep turtle's drawing in view for larger polygons
	# pu(Turtle) 
	# rt(Turtle)
	# fd(Turtle,100)
	# pd(Turtle)
	angle = 360.0/n
	for i in range(n):
		fd(Turtle,len)
		lt(Turtle,angle)

polygon(lee,50,5)










wait_for_user()					
