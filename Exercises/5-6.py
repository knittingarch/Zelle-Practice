'''
A program that calculates the total value of a person's full name.
by Sarah Dawson
'''

def main():

	print 'This program will tell you how many points each letter of your name is worth and tally the total for your full name!'
	print 'It uses the standard a=1, b=2, c=3, etc.'

	full_name = raw_input('Please enter your full name here: ')
	low_name = full_name.lower()
	single_name = low_name.split(" ")
	
	# Creates empty bucket to receive the values that are going to be calculated below.
	tally = 0

	# Isolate each name
	for item in single_name:
		# Grab each letter in a single name	
		for l in item:
			# Take the letter, convert it to the ASCII number, and then subtract 96 to get the alpha number value
			number = ord(l) - 96
			print l + '=' + str(number) + ',',
			# Adds each value to tally
			tally += number

	print '\nWoot!  Your full name adds up to a total of', tally, 'points!'		

		
main()	
