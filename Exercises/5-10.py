'''
A program that calculates the average word length in a sentence entered by the user.
by Sarah Dawson
'''

def main():
	print 'This program will calculate the average word length in the sentence you enter.\n'

	phrase = raw_input('Please enter your sentence here: ')
	split_phrase = phrase.split()
	tally = 0.0

	for words in split_phrase:
		# adds the length of each word to tally
		tally += len(words)
		# print tally

	avg_length = tally / len(split_phrase)

	print '\nThere are', len(split_phrase), 'words in this sentence, and the average word length is {0:0.2f}.'.format(avg_length)

main()