'''
A program that accepts an exam score between 0-100 and asigns a letter grade based on 10-pt scale (90-100 = A, etc)
This program uses list sequencing, although a simple if/elif/else statement with integers would work as well.
by Sarah Dawson
'''

def main():

	print 'This program will convert your numerical grade into a letter grade. \n'

	grade = eval(raw_input('Please enter your grade here: '))
	numbers = []

	for i in range(101):
		numbers.append(i)

	if grade >= numbers[90]:
		print 'You earned an A.'
	elif numbers[80] < grade < numbers[90]:
		print 'You earned an B.'
	elif numbers[70] < grade < numbers[80]:
		print 'You earned an C.'
	elif numbers[60] < grade < numbers[70]:
		print 'You earned an D.'
	else:
		print 'You earned an F'

main()
