'''
A program that calculates the height of a ladder for a given height with the ladder leaned against a house
by Sarah Dawson
'''

import math

def main():
	print "This program will help you choose the right length for your ladder!"
	height = eval(raw_input("Please enter the height you need to reach in feet: "))
	degrees = eval(raw_input("Please enter the angle of lean in degrees: "))
	angle_in_radians = (math.pi / 180) * degrees
	print angle_in_radians
	length = (height / math.sin(angle_in_radians))
	print "You need a ladder that is", length, "feet long."

main()	

0.20791169081