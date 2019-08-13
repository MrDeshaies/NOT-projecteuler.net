import math
from euler import *

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isDivisibleAll(number,max):
	for x in range(2,max+1):
		if number % x != 0:
			return False
	return True


def find005Answer():
	x = 20
	# likely candidate for 20 is 1,862,340,480.
	# if reach >>2e9, something is wrong
	dangerZone = 2e9 * 4
	while True:
		#test divisibility
		if isDivisibleAll(x,20):
			print("And the winner is... " + str(x))
			print("Its factors are " + str(fact(x)))
			return

		if x > dangerZone:
			print("Reached " + str(x) + " and didn't find it yet..")
			return
		# increment...
		x = x+1


def find005AnswerFast():
	# factorials by their nature are close to what is desired.
	# E.g. we know that 5!=120 will be divisible by all the number from 1 to 5
	#      since it is by definition 1*2*3*4*5.
	# The 20! is a LARGE number, but it's likely one of its factors meets the condition.
	# I got lucky in the way that it met the condition of being the smallest such number
	# (I didn't prove that it would be the case)
	i = math.factorial(19)
	for x in fact(i):
		if isDivisibleAll(x,20):
			print("And the winner is... " + str(x))
			for k in range(2,21):
				print(str(x) + " / " + str(k) + " = " + str(x/k))
			print("Its factors are " + str(fact(x)))
			return
	print("not found")

find005AnswerFast()
