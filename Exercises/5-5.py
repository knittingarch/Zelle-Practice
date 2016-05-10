'''
A script that assigns a numerical value to each letter of the alphabet, takes a user-inputted name, and calculates and returns the value of a singular name
by Sarah Dawson
'''

def main():

	print 'This program will tell you how many points each letter of your name is worth and tally the total!'
	print 'It uses the standard a=1, b=2, c=3, etc.'

	name = raw_input('Please type one name here: ')
	low_name = name.lower()

	tally = 0

	for l in low_name:
		# gets the ascii number for the letter and subtracts 96 to get the actual number if starting at 1
		number = ord(l) - 96
		print l + '=' + str(number) + ',',
		tally += number
	
	print '\nOooh!  Your name adds up to a total of', tally, 'points.'
	
main()		