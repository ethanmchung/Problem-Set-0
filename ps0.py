def bool_even_or_odd(number):
	''' Problem #0 '''
	oddOrEven = number%2
	#since even numbers are all divisible by 2 but 2 does not go evenly into odd numbers, 
	#the mod function is used to test for the remainder of the inputted number

	if oddOrEven == 0:
		return(True)
	
	if oddOrEven == 1:
		return(False)


def number_of_digits(number):
	''' Problem #1 '''
	x = 1
	y = 2
	if number in range(10):
		digits = 1
	else:
		while number not in range(10**x, 10**y):
			x = x + 1
			y = y + 1
			digits = y
	return(digits)


def sum_of_digits(number):
	''' Problem #2 '''
	sum = 0
	while number > 0:
		sum += number % 10
		number = number//10
	return(sum)


def sum_less_ints(number):
	''' Problem #3 '''
	list = []
	while number != 0: # this loop results in a list with all of the numbers less than the initial user's number
		number = number - 1
		list.append(number)

	x = 0
	for numb in list: # this loop adds together all of the numbers less than the initial user's number
		x = x + numb
	return(x)
	

def factorial(number):
	''' Problem #4 '''
	list = []
	
	while number != 0: 
	#this loop results in a list with all of the numbers that will be needed to be multiplied later on
		list.append(number)
		number = number - 1
	
	x = 1
	for numb in list:
	#this loop multiplies all of the necessary numbers together in order to get the answer to the factorial
		x = x * numb
	return(x)


def evenly_divisible(first, second):
	''' Problem #5 '''
	remainder = first%second
	# the mod function is used because the remainder will indicate whether the second number goes in evenly or not
	# if the remainder is 0, then the second number went into the first number evenly
	# but if there is a remainder, then the second number did not go into the first number evenly
	if remainder == 0:
		answer = True
	else:
		answer = False
	return(answer)


def prime(number):
	''' Problem #6 '''
	if number <= 1: # because primes are integers greater than one
		answer = False
	else:
		rangeOfNumber = range(2, number)
		x = 0
		# this loop tracks whether or not there are any numbers that divide evenly into the original number
		for numb in rangeOfNumber:
			if number%numb == 0:
				x = 1
		if x == 1:
		# if there are any numbers in the rangeOfNumber that divide evenly into the original number,
		#then the initial number is not a prime
			answer = False
		if x == 0: # if there are not any numbers in the rangeOfNumber that divide evenly into the original number,
		#then the initial number is a prime, since the only other factors must be one and the number itself
			answer = True
	
	return(answer)


def perfect(number):
	''' Problem #7 '''
	if number <= 0:
		answer = False
	else:
		list = []
		for numb in range(1, number): #this loop checks and records the proper factors of the number
			remainder = number%numb
			if remainder == 0:
				list.append(numb)
		x = 0 
		# x will be the value of the sum of the proper factors
		# for every item in the list, that number is repeatedly added until the total sum of the factors is reached
		for factor in list: 
			x = x + factor
	
		if x == number: #if the sum of the of the proper factors is equal to the number, then it is a perfect numbers
			answer = True
		else:
			answer = False
	
	return(answer)


def sum_evenly(number):
	''' Problem #8 '''
	y = sum_of_digits(number)
	remainder = number%y
	# the mod function is used because the remainder will indicate whether the sum of the digits number goes in evenly or not
	# if the remainder is 0, then the sum of the digits of the number went into the number evenly
	# but if there is a remainder, then the sum of the digits of the number did not go into the number evenly
	if remainder == 0:
		answer = True
	else:
		answer = False
	
	return(answer)