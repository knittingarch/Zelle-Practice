''' file: chaos.py
A simple program illustrating chaotic behavior.'''

def main():
	print("This program illustrates a chaotic function")
	x = eval(raw_input("Enter a number between 0 and 1: "))
	y = eval(raw_input("Enter a number between 0 and 1: "))
	for i in range(15):
		x = 3.9 * x * (1 - x)
		y = 3.9 * y * (1 - y)
		print x, y

# def main_two():
# 	print("This program illustrates a chaotic function")
# 	x = eval(input("Enter a number between 0 and 1: "))
# 	for i in range(100):
# 		x = 3.9 * (x - x * x)
# 		print(x)

# def main_three():
# 	print("This program illustrates a chaotic function")
# 	x = eval(input("Enter a number between 0 and 1: "))
# 	for i in range(100):
# 		x = 3.9 * x - 3.9 * x * x
# 		print(x)


main()
# main_two()
# main_three()