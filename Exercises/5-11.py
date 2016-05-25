''' A simple program illustrating chaotic behavior.
Formatting by Sarah Dawson'''

def main():
	print("This program illustrates a chaotic function")
	x = eval(raw_input("Enter a number between 0 and 1: "))
	y = eval(raw_input("Enter a number between 0 and 1: "))

	# Create table labels
	print '\n{0:^10} {1:^15.2f} {2:^15.2f}'.format("index", x, y)

	# Create horizontal rule
	print "-"*41	

	# Iterate through items and apply formula
	for i in range(15):
		x = 3.9 * x * (1 - x)
		y = 3.9 * y * (1 - y)
		# Print out the values in a formatted table
		print '{0:^10} {1:^15.6f} {2:^15.6f}'.format(i, x, y)

main()