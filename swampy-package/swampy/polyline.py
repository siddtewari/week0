import math
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

bob.delay = .01

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

polyline(bob, 5, 10, 60)


wait_for_user()