#The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?

def f(n):
	if n%2 == 0:
		return n/2
	else:
		return 3*n + 1

def collatz(x):
	result = [x]
	while x != 1:
		x = f(x)
		result.append(x)
	return result

maxLen=0
maxNum=0

stop = 1000000

x=1
while x < stop:
	xLen = len(collatz(x))
	#print str(x) + ": " + str(collatz(x))
	if xLen > maxLen:
		maxLen = xLen
		maxNum = x
		print(str(maxLen) + " with starting number " + str(maxNum))
	x += 1
print(str(maxLen) + " with starting number " + str(maxNum))
