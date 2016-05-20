import ps0

print("This is problem #0")
userNumber = 0
print("Is " + str(userNumber) + " an even number?: " + str(ps0.bool_even_or_odd(userNumber)))
userNumber = 3
print("Is " + str(userNumber) + " an even number?: " + str(ps0.bool_even_or_odd(userNumber)))
userNumber = 48
print("Is " + str(userNumber) + " an even number?: " + str(ps0.bool_even_or_odd(userNumber)))


print("\nThis is problem #1")
userNumber = 10
print(str(userNumber) + " has " + str(ps0.number_of_digits(userNumber)) + " digits.")
userNumber = 0
print(str(userNumber) + " has " + str(ps0.number_of_digits(userNumber)) + " digits.")
userNumber = 1
print(str(userNumber) + " has " + str(ps0.number_of_digits(userNumber)) + " digits.")
userNumber = 123456789
print(str(userNumber) + " has " + str(ps0.number_of_digits(userNumber)) + " digits.")


print("\nThis is problem #2")
userNumber = 0
print("The sum of the digits of " + str(userNumber) + " is {}.".format(ps0.sum_of_digits(userNumber)))
userNumber = 1
print("The sum of the digits of " + str(userNumber) + " is {}.".format(ps0.sum_of_digits(userNumber)))
userNumber = 556473
print("The sum of the digits of " + str(userNumber) + " is {}.".format(ps0.sum_of_digits(userNumber)))
userNumber = 642
print("The sum of the digits of " + str(userNumber) + " is {}.".format(ps0.sum_of_digits(userNumber)))


print("\nThis is problem #3")
userNumber = 0
print("The sum of all the integers that are less than the number {} is {}.".format(userNumber, ps0.sum_less_ints(userNumber)))
userNumber = 1
print("The sum of all the integers that are less than the number {} is {}.".format(userNumber, ps0.sum_less_ints(userNumber)))
userNumber = 6
print("The sum of all the integers that are less than the number {} is {}.".format(userNumber, ps0.sum_less_ints(userNumber)))


print("\nThis is problem #4")
userNumber = 0
print("The factorial of the number {} is {}.".format(userNumber, ps0.factorial(userNumber)))
userNumber = 1
print("The factorial of the number {} is {}.".format(userNumber, ps0.factorial(userNumber)))
userNumber = 4
print("The factorial of the number {} is {}.".format(userNumber, ps0.factorial(userNumber)))


print("\nThis is problem #5")
First = 5
Second = 3
print("Is " + str(Second) + " a factor of " + str(First) + "?: " + str(ps0.evenly_divisible(First, Second)))
First = 3
Second = 3
print("Is " + str(Second) + " a factor of " + str(First) + "?: " + str(ps0.evenly_divisible(First, Second)))
First = 1
Second = 3
print("Is " + str(Second) + " a factor of " + str(First) + "?: " + str(ps0.evenly_divisible(First, Second)))
First = 12
Second = 3
print("Is " + str(Second) + " a factor of " + str(First) + "?: " + str(ps0.evenly_divisible(First, Second)))


print("\nThis is problem #6")
userNumber = 1
print("Is " + str(userNumber) + " a prime number?: " + str(ps0.prime(userNumber)))
userNumber = 2
print("Is " + str(userNumber) + " a prime number?: " + str(ps0.prime(userNumber)))
userNumber = 5
print("Is " + str(userNumber) + " a prime number?: " + str(ps0.prime(userNumber)))
userNumber = 10
print("Is " + str(userNumber) + " a prime number?: " + str(ps0.prime(userNumber)))


print("\nThis is problem #7")
userNumber = 1
print("Is " + str(userNumber) + " a perfect number?: " + str(ps0.perfect(userNumber)))
userNumber = 6
print("Is " + str(userNumber) + " a perfect number?: " + str(ps0.perfect(userNumber)))
userNumber = 10
print("Is " + str(userNumber) + " a perfect number?: " + str(ps0.perfect(userNumber)))


print("\nThis is problem #8")
userNumber = 1
print("Does the sum of the digits of the number " + str(userNumber) + " divide evenly into that same number?: " + str(ps0.sum_evenly(userNumber)))
userNumber = 31
print("Does the sum of the digits of the number " + str(userNumber) + " divide evenly into that same number?: " + str(ps0.sum_evenly(userNumber)))
userNumber = 42
print("Does the sum of the digits of the number " + str(userNumber) + " divide evenly into that same number?: " + str(ps0.sum_evenly(userNumber)))