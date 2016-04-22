'''
A program that calculates the total cost of a coffee order based on weight, price and shipping
by Sarah Dawson
'''

def main():
	print "Welcome to the Coffee Cost Calculator!"
	weight = eval(raw_input("How many pounds of coffee would you like? "))
	price = weight * 10.50
	shipping = weight * 0.86
	overhead = 1.50
	total_cost = price + shipping + overhead
	print "Your order comes to", total_cost, "including shipping and fees."

main()	