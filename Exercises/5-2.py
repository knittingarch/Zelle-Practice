'''
A program to assign letters to numerical grades.
by Sarah Dawson
'''


def main():
	letter_grade = ['F', 'F', 'D', 'C', 'B', 'A']
	num_grade = eval(raw_input("Please enter your numerical grade (1-5): "))
	print "You earned a ", letter_grade[num_grade], "on that quiz."

main()	