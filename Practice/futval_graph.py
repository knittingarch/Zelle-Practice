'''
futval program converted to graphical interface
'''

from graphics import *

def main():
	# Introduction
	print "This program plots the growth of a 10-year investment."

	# Get principal and interest rate
	principal = eval(raw_input("Enter the initial principal: "))
	apr = eval(raw_input("Enter the annualized interest rate: "))

	# Create a graphics window with labels on left side
	win = GraphWin("Investment Growth Chart", 320, 240)
	win.setBackground("white")
	win.setCoords(-1.75, -200, 11.5, 10400)
	# win.setCoords(0.0, 0.0, 10.0, 10000.0)
	Text(Point(-1, 0), '0.0K').draw(win)
	Text(Point(-1, 2500), '2.5K').draw(win)
	Text(Point(-1, 5000), '5.0K').draw(win)
	Text(Point(-1, 7500), '7.5K').draw(win)
	Text(Point(-1, 10000), '10.0K').draw(win)

	# Draw bar for initial principal
	height = principal * 0.02
	bar = Rectangle(Point(0, 0), Point(1, principal))
	# bar = Rectangle(Point(year, 0), Point(year + 1, principal))
	# bar = Rectangle(Point(40, 230), Point(65, 230-height))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	# Draw bars for successive years
	for year in range(1, 11):
		# calculate the value for the next year
		principal = principal * (1 + apr)
		bar = Rectangle(Point(year, 0), Point(year + 1, principal))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	raw_input("Press <Enter> to quit")	
	win.close()

main()	

