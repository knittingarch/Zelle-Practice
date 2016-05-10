'''
A script that assigns a numerical value to each letter of the alphabet, takes a solitary user-inputted name, and calculates and returns the value of a singular name
by Sarah Dawson
'''

def main():

	print 'This program will tell you how many points your name is based on a=1, b=2, etc.'

	name = raw_input('Please type one name here: ')
	low_name = name.lower()

	tally = 0

	for l in low_name:
		number = ord(l) - 96
		print l + '=' + str(number) + ',',
		tally += number
	
	print '\nOooh!  You name adds up to a total of', tally, 'points.'
	
main()		