'''
Simple way to encode a user-provided message
'''

def main():
	print "This program converts a textual message into a sequence"
	print "of numbers representing the Unicode encoding of the message. \n"

	# get the message to encode
	message = raw_input("Please enter the message to encode: ")

	print "Your encoded message is: "
	
	# loop through the message and print out the Unicode values
	for ch in message:
		print ord(ch),


main()		