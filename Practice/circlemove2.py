'''
A program that allows a user to draw a red square and then move (or draw) it 10 times.

'''

from graphics import *

def main():
	win = GraphWin()
	shape = Rectangle(Point(10,10), Point(30,30))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()
		dx = p.getX() - c.getX()
		dy = p.getY() - c.getY()
		# shape.move(dx,dy)
		new = shape.clone()
		new.move(dx,dy)
		new.draw(win)
	win.close()
	
main()		
