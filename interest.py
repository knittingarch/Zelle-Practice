'''
Program to calculate the future value of an investment
Includes initial deposit and annual percentage rate
'''

'''
Changes the program to allow the investment years to be input by user.
'''
def main():
	print "Welcome to the investment interest calculator!"

	deposit = eval(raw_input('Please tell me how much you plan to deposit: '))
	fixed_amount = 10
	interest_years = eval(raw_input('And how many years do you plan to grow your money? '))

	for y in range(interest_years):
		deposit += fixed_amount

	print 'In', interest_years, 'you will have a total value of', deposit, '.'

main()

# def main():
# 	print raw_input('Welcome to the investment interest calculator!')

# 	deposit = eval(raw_input('Please tell me how much you plan to deposit: '))
# 	apr = eval(raw_input('How much is your annual percentage rate? '))
# 	# interest_years = raw_input('And how many years do you plan to grow your money? ')

# 	for y in range(10):
# 		deposit += (deposit * apr)
	
# 	print 'The value in 10 years will be ', deposit


# main()


# '''
# Changes the program to allow the investment years to be input by user.
# '''
# def main():
# 	print "Welcome to the investment interest calculator!"

# 	deposit = eval(raw_input('Please tell me how much you plan to deposit: '))
# 	apr = eval(raw_input('How much is your annual percentage rate in decimals? '))
# 	interest_years = eval(raw_input('And how many years do you plan to grow your money? '))

# 	for y in range(interest_years):
# 		deposit += (deposit * apr)

# 	print 'In', interest_years, 'you will have a total value of', deposit, '.'

# main()



