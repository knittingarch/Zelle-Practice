'''
A program that prints a file to the screen.
'''

def main():
	fname = raw_input("Enter filename: ")
	infile = open(fname, "r")
	for i in range(5):
		data = infile.readline()
		print(data[:-1])

main()	