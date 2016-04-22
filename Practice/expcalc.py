'''
A program to allow users to enter and receive the value of their own expressions 
by: Sarah Dawson
'''

def main():
	print "Welcome to your very own expression calculator! Enter an expression and see the results instantly!"
	for n in range(100):
		answer = eval(raw_input("Please enter your expression: "))
		print answer

main()
