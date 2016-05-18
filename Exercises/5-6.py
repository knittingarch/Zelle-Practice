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
	
	print low_name
	print single_name
	
	tally = 0

	for item in single_name:
		for l in item:
			number = ord(l) - 96
			print l + '=' + str(number) + ',',
			tally += number

	print '\nWoot!  Your full name adds up to a total of', tally, 'points!'		

	# tally = 0

	# for l in low_name:
	# 	# gets the ascii number for the letter and subtracts 96 to get the actual number if starting at 1
	# 	number = ord(l) - 96
	# 	print l + '=' + str(number) + ',',
	# 	tally += number
	
	# print '\nOooh!  Your name adds up to a total of', tally, 'points.'
	
main()	
