'''
A program that makes acronyms out of user-provided phrases.
by Sarah Dawson
'''

def main():
	acronym = ""
	phrase = raw_input("Please enter your phrase: ")
	phrase = phrase.split(" ")
	for s in phrase:
		acronym += s[0].upper()

	print acronym	

main()		