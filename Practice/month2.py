'''
A program that assigns abbreviations to months based on list sequencing.
'''


def main():

	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
			  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

	n = eval(raw_input("Please select a month from 1 - 12: "))

	monthsAbbrev = months[n - 1]

	print "The month abbreviation for", n, "is " + monthsAbbrev + "."


main()	