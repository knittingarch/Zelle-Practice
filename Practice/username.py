'''
A program that creates usernames from string inputs.

by Sarah Dawson
'''

def main():

	print "This program generates computer usernames. \n"

	# get user's first and last names
	firstname = raw_input("Please enter your first name: ")
	lastname = raw_input("Please enter your last name: ")

	# concatenate first initial with first 7 chars of last name
	username = firstname[0].lower() + lastname[:7].lower()
	
	# print out username
	print "Your username is ", username

main()	