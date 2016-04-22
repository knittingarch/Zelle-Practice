'''
A program that will convert Celsius to Fahrenheit
by: Sarah Dawson
'''

def main():
	print "Welcome to the Temperature Converter! It will tell you what the temperature is in Celsius!"

	fahrenheit = eval(raw_input('Please enter the temperature in Fahrenheit: '))
	celsius = (fahrenheit - 32) * (5.0/9.0)
	
	print "The temperature is", celsius, "Celsius."

main()	