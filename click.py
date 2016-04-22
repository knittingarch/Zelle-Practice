'''
A program to get mouse clicks using getMouse (4.7.1)
'''

from graphics import *

def main():
	win = GraphWin("Click Me!")
	for i in range(10):
		p = win.getMouse()
		print "You clicked at:", p.getX(), p.getY()
	win.close()

main()		