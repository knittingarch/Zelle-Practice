# Refactoring Exercise 3-16.py (calculate the nth Fibonacci number) using functions
# by Sarah Dawson


print "This program will return the Fibonacci number based on your input!"
number = eval(raw_input("Please enter the number you would like to check: "))


def fibonacci(n):
	# Initiate variable
	a, b = 1, 1
	for i in range(n - 1):
		# Set up simultaneous assignment to facilitate accumulation
		a, b = b, a + b
	print "The fibonacci number at index " + str(n) + " is " + str(a) + "."
	return a


fibonacci(number)