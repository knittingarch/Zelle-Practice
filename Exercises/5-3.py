'''
A program that accepts an exam score between 0-100 and asigns a letter grade based on 10-pt scale (90-100 = A, etc)
by Sarah Dawson
'''

def main():

	grade = eval(raw_input('Please enter your grade here: '))

	if 90 <= grade <=100:
		print 'A'
	elif 80 < grade < 90:
		print 'B'
	elif 70 < grade < 80:
		print 'C'
	elif 60 < grade < 70:
		print 'D'
	else:
		print 'F'

main()
