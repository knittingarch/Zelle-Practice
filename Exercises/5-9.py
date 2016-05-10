'''
A program that counts the number of words in a sentence entered by a user
by Sarah Dawson
'''

def main():

	print 'This program will calculate the number of words in your sentence.\n'

	phrase = raw_input('Please enter your phrase here: ')
	split_phrase = phrase.split()

	print 'Your phrase has', len(split_phrase), 'words.'

main()	