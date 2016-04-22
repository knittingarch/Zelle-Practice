'''
A program that creates an archery target with 5 concentric circles of the same width.
By Sarah Dawson
'''

from graphics import *

def main():
	win = GraphWin("Bullseye", 300, 300)
	win.setBackground("grey")
	start = 100
	width = 20
	white = Circle(Point(150, 150), start)
	white.setFill("white")
	white.setOutline("white")
	white.draw(win)
	black = Circle(Point(150, 150), start - width)
	black.setFill("black")
	black.setOutline("black")
	black.draw(win)
	blue = Circle(Point(150, 150), start - 2 * width)
	blue.setFill("blue")
	blue.setOutline("blue")
	blue.draw(win)
	red = Circle(Point(150, 150), start - 3 * width)
	red.setFill("red")
	red.setOutline("red")
	red.draw(win)
	yellow = Circle(Point(150, 150), start - 4 * width)
	yellow.setFill("yellow")
	yellow.setOutline("yellow")
	yellow.draw(win)

	input("Press <Enter> to quit")
	win.close()	


main()	