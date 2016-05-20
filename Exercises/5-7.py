'''
A simple Caesar cipher that shifts letters a variable number of spaces based on user input. This 
program will encode and decode messages using the cipher and circular alphabet.  
**Improvement would be keeping blank spaces and punctuation.**
by Sarah Dawson
'''

def main():
	phrase = raw_input("Please enter your phrase: ").lower()
	key = eval(raw_input("Please enter the number you want to shift the letters by: "))

	encoded = []

	# Separates phrase into # of words	
	for item in phrase:
		for l in item:
			# Checks if character if a letter
			if l.isalpha():
				# Finds ASCII number and adds key to it	
				number = ord(l) + key
				# Checks if letter is past the end of the alphabet
				if number > ord('z'):
					# Subtracts 26 for that letter's number to get it back in range
					number -= 26
				# Turns the key-added number back into a letter and appends to empty list
				encoded.append(chr(number))

	# Joins all of the letters fromthe encoded list into a string		
	encoded_message = ''.join(encoded)
	print "\nThe encoded message is:", encoded_message

	decoded = []

	for l in encoded_message:
		letter = ord(l) + (-key)
		if letter < ord('a'):
			letter += 26
		# Finds ASCII number and subtracts the key from it
		decoded.append(chr(letter))

	decoded_message = ''.join(decoded)	
	print "\nThe decoded message is:", decoded_message

main()				