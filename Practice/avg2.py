''' avg2.py
	A simple program to average three exam scores
	Illustrates use of multiple inputs '''


def main():
	print("This program computes the average of three exam scores.")

	score1, score2, score3 = eval(raw_input("Enter three scores separated by a comma: "))
	average = (score1 + score2 + score3) / 3

	print "The average of the three scores is:", average

main()		