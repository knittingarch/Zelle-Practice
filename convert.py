'''
A program to convert Celsius temps to Fahrenheit
by: Susan Computewell
'''

# def main():
# 	for t in range(5):
# 		celsius = eval(raw_input("What is the Celsius temperature? "))
# 		fahrenheit = (1.8 * celsius) + 32
# 		print "The temperature is", fahrenheit, "degrees Fahrenheit."


'''
Change program to print table of results every 10 degrees from 0-100
'''
def main():
	for t in range(0, 101,10):
		fahrenheit = (9.0/5.0 * t) + 32
		print "Celsius", "Fahrenheit"
		print t, fahrenheit

main()	