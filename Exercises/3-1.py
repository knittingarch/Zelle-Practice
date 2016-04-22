'''
A program that calculates the volume and surface area of a sphere
by Sarah Dawson
'''
import math

def main():
	print "This program will caluclate the volume and surface area of a sphere with your help!"
	r = eval(raw_input("Please enter the radius of your sphere: "))
	volume = 4.0/3.0 * math.pi * r**3
	area = 4 * math.pi * r**2
	print volume
	print area

main()	