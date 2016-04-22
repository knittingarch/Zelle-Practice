'''
A program that assigns abbreviations to months based on string location.
'''

def main():
	print "This programs prints out a month's abbreviation based on integer input."

	# put all abbreviation in one strin
	months = "JanFebMarAprMayJunJulAugSepOctNovDec"

	# get integer that represents month from user
	n = eval(raw_input("Please select a month from 1 - 12: "))

	# calculate position in str
	start = (n - 1) * 3
	finish = start + 3

	# use str sequence to get abbreviation
	monthsAbbrev = months[start:finish]

	# print out abbreviation
	print start, finish
	print "The abbreviation for ", n, "is ", monthsAbbrev, "."


main()	