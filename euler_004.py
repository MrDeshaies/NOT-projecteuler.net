#Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(str):
	return str[::-1]
	

def isPalindrome(number):
	return str(number) == reverse(str(number))

#Find the largest palindrome made from the product of two 3-digit numbers.
def find004Answer():
	largestProd = 0
	largestX = 0
	largestY = 0
	
	# start at the top and iterate down...
	for x in range(999,99,-1):
		for y in range(999,99,-1):
			prod = x*y
			if prod > largestProd and isPalindrome(prod):
				largestProd = prod
				largestX = x
				largestY = y
	print("Final answer:")
	print(str(largestX) + " x " + str(largestY) + " = " + str(largestProd))

find004Answer()
