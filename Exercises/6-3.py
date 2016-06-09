# Refactoring Exercise 3-1.py (calculate the volume and surface area of a sphere) using functions
# by Sarah Dawson


import math

print "This program will caluclate the volume and surface area of a sphere with your help!"
radius = eval(raw_input("Please enter the radius of your sphere: "))

def sphereArea(radius):
	print 4 * math.pi * radius**2

def sphereVolume(radius):	
	print 4.0/3.0 * math.pi * radius**3


sphereArea(radius)
sphereVolume(radius)	