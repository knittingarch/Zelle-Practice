'''
A program that creates an archery target with 5 concentric circles of the same width.
By Sarah Dawson
'''

from graphics import *

def main():
	win = GraphWin("Bullseye", 300, 300)
	win.setBackground("grey")
	colors = ["white", "black", "blue", "red", "yellow"]
	# largest diameter
	start = 100
	# width of the visible rings
	width = 20
	# begin for loop
	for i in range(5):
		# calculates diminishing radii for each of 5 circles
		radius = start - (i * width)
		# grabs name color as string so it can be passed below
		bgcolor = colors[i]
		# creates the circle object
		x = Circle(Point(150, 150), radius)
		# following code sets colors and draws object in window
		x.setFill(bgcolor)
		x.setOutline(bgcolor)	
		x.draw(win)

	win.getMouse() # waits for user click before executing the next command
	# win.close()

main()	