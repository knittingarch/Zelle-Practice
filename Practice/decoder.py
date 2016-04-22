'''
Simple way to DECODE a user-provided message that was encoded using Unicode
by Sarah Dawson
'''

def main():
	print "This program take a Unicode coded message and"
	print "returns the message in Latin text characters. \n"

	# get the numbers to decode and create empty string to hold future decoded message
	coded = eval(raw_input("Please enter the message to encode (surrounded by quotation marks): "))
	decodedMsg = ""
	print "\nYour original message was: ", coded
	
	# loop through the message and convert strings to integers
	for n in coded.split():
		decoded = int(n)
		
		# accumulate the decoded characters into the empty string 
		decodedMsg += chr(decoded)

	# print out decoded message	
	print "Your decoded message is:", decodedMsg
	

main()		