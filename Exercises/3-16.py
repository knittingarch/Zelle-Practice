# A program to calculate the nth Fibonacci number where n is a value input by the user.
# by Sarah Dawson


def main():
	print "This program will return the Fibonacci number based on your input!"
	n = eval(raw_input("Please enter the number you would like to check: "))

	a, b = 1, 1
	for i in range(n - 1):
		a, b = b, a + b

	print "The fibonacci number at index " + str(n) + " is " + str(a) + "."


main()	
