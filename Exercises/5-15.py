'''
A program that reads student test scores from a file and displays the data with a horizontal bar chart.
by Sarah Dawson
'''

from graphics import *

def main():
	print("This program takes last names and test scores from a file, and returns a graph of each student's results.")

	with open("student_scores.txt", "r") as f:
		count = f.readline()

		# Create a graphics window
		win_height = 200
		win_width = 400
		win = GraphWin("Student Exam Scores", win_width, win_height)
		win.setBackground("grey")

		# Add horizontal labels to improve display

		# Set up empty accumulator
		entry = 0

		# Iterate through the lines of the file
		for line in f:

			# Split the data to make access easier
			data = line.split()
			
			# Grab the name
			name = data[0]

			#Grab the score
			score = data[1]

			#Accumulate
			entry += 1

			# Set desired bar thickness
			height = 20

			# Calculate length for the window size based on score
			width = (int(score) * win_width / 100) - 60

			# Calculate coordinates using above variables
			point1x = height
			point1y = (win_height - (height * entry))
			point2x = width
			point2y = (win_height - (height * (entry) - height))
			
			# Add spacing after and above the label
			name_labelx = point1x + 18
			name_labely = point1y + 8

			# Create labels on left side
			Text(Point(name_labelx, name_labely), name).draw(win)

			# Create bar for each entry in file
			bar = Rectangle(Point((height + 55),(win_height - (height * entry))), Point((width + 55), (win_height - (height * entry - height))))

			bar.setWidth(1)
			bar.setFill("blue")
			bar.setOutline("white")
			bar.draw(win)

	
		win.getMouse()
		win.close()

main()	