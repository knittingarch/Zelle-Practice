# Refactoring Exercise 3-2.py (calculate the cost per square inch of a circular pizza) using functions
# by Sarah Dawson


import math


print "This program calculates the cost per square inch of circular pizza."
diameter = eval(raw_input("Please enter the pizza's diameter in inches: "))
price = eval(raw_input("Please enter the total cost of the pizza (using decimals): "))


def pizzaArea(size):
	radius = size/2
	return math.pi * radius**2

area = pizzaArea(diameter)

def squareInchCost(cost):
	inch_cost = cost / area
	inch_cost_in_cents = round(inch_cost, 2)
	print "This delicious pizza costs", inch_cost_in_cents, "per inch."


squareInchCost(price)
