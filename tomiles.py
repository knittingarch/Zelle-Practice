'''
A program that converts kilometers to miles
by: Sarah Dawson
'''

def main():
	print "Welcome to the Distance converter!"

	kilometers = eval(raw_input("How many kilometers are we talking about? "))
	miles = kilometers * 0.62

	print "That's", miles, "miles!"

main()	