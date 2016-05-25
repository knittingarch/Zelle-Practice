'''
A program that counts the number of lines, words, and characters in an external file.
by Sarah Dawson
'''

def main():
	print "This program will count the number of lines, words, and characters in the file provided."	

	# Open file and assign all lines to variable
	with open("BobRoss.txt", "r") as f:
		
		# Create empty buckets for accumulation
		lines = 0
		words = 0
		characters = 0

		# Iterate through lines, words, and characters and add each tick to above bucket
		for line in f:
			lines += 1

			# Split each sentence up into words so they can be counted individually
			for word in line.split():
				words += 1

				# Count each character in each word
				for ch in word:
					characters += 1

		# Print results with string formatting			
		print "This document contains {0} lines, {1} words, and {2} characters in total.".format(lines, words, characters)


main()