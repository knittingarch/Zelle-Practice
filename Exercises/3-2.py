'''
A program to calculate the cost per square inch of a circular pizza
by Sarah Dawson
'''

import math

def main():
	print "This program calculates the cost per square inch of circular pizza."
	diameter = eval(raw_input("Please enter the pizza's diameter in inches: "))
	price = eval(raw_input("Please enter the total cost of the pizza (using decimals): "))
	radius = diameter/2
	area = math.pi * radius**2
	inch_cost = price / area
	inch_cost_in_cents = round(inch_cost , 2)
	print "This delicious pizza costs", inch_cost_in_cents, "per inch."

main()	
