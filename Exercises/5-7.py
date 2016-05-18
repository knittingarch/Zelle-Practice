'''
A simple Caesar cipher that shifts letters a variable number of spaces based on user input. This 
program will encode and decode messages using the cipher.  **Improvement would be changing the 
blank spaces from " to an actual blank space and removing punctuation.**
by Sarah Dawson
'''

def main():
	phrase = raw_input("Please enter your phrase: ")
	key = eval(raw_input("Please enter the number you want to shift the letters by: "))

	encoded = []

	# Separates phrase into # of words	
	for item in phrase:
		for l in item:
			# Finds ASCII number and adds key to it	
			number = ord(l) + key
			# Turns the key-added number back into a letter and appends to empty list
			encoded.append(chr(number))

	# Joins all of the letters fromthe encoded list into a string		
	encoded_message = ''.join(encoded)
	print "\nThe encoded message is:", encoded_message

	decoded = []

	for l in encoded_message:
		# Finds ASCII number and subtracts the key from it
		letter = ord(l) + (-key)
		decoded.append(chr(letter))

	decoded_message = ''.join(decoded)	
	print "\nThe decoded message is:", decoded_message


main()				