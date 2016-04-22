'''
A program to calculate the area of a three-sided triangle
by Sarah Dawson
'''

import math

def main():
	print "Welcome to the Triangle Area-Finding Machine!"
	a, b, c = eval(raw_input("Please enter the three sides of your triangle in inches (separated by commas): "))
	s = (a + b +c)/2
	area = math.sqrt(s * ((s-a) * (s-b) * (s-c)))
	rounded_area = round(area, 2)
	print "The area of a triangle with", a, b, "and", c, "as lengths, is", rounded_area, "."

main()	