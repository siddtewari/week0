world.clear()
bob = Turtle()
def ltfd(turtle, n):
 lt(turtle)
 fd(turtle, n)

def trnArd(turtle):
 rt(turtle)
 rt(turtle)

def fdLt(turtle,n):
 fd(turtle,n)
 lt(turtle)

def rtFd(turtle,n):
 rt(turtle)
 fd(turtle,n)

def ltFd(turtle,n):
 lt(turtle)
 fd(turtle,n)

def retrace(turtle,n):
 trnArd(turtle)
 fd(turtle,n)

def detachL(turtle,n):
 pu(turtle)
 lt(turtle)
 fd(turtle,n)
 pd(turtle)

def detachW(turtle,n):
 pu(turtle)
 lt(turtle)
 fd(turtle,n)
 pd(turtle)

def drawH():
 ltFd(bob,20)
 trnArd(bob)
 fdLt(bob,10)
 fdLt(bob,14)
 fd(bob,10)
 trnArd(bob)
 fd(bob,20)
 detachL(bob,10)

def drawE():
 ltFd(bob,20)
 rtFd(bob,10)
 retrace(bob,10)
 ltFd(bob,10)
 ltFd(bob,8)
 retrace(bob,8)
 ltFd(bob,10)
 ltFd(bob,10)
 rt(bob)
 detachL(bob,10)

def drawL():
 ltFd(bob,20)
 retrace(bob,20)
 ltFd(bob,14)
 rt(bob)
 detachL(bob,10)

def drawO():
 ltFd(bob,20)
 rtFd(bob,12)
 rtFd(bob,20)
 rtFd(bob,12)
 retrace(bob,12)
 rt(bob)
 detachL(bob,20)
 
drawH()
drawE()
drawL()
drawL()
drawO()