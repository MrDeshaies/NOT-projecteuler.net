import re

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


toTwenty = ["","one","two","three","four","five","six","seven","eight","nine","ten",
	"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def zeroToNine(x):
	return toTwenty[x%10]

def zeroToTwenty(x):
	return toTwenty[x%20]

def zeroToHundred(x):
	if x < 20:
		return zeroToTwenty(x)
	
	unit = zeroToNine(x%10)
	ten = tens[(x%100) // 10]
	result = ten
	if unit != "":
		result += "-" + unit
	return result

def zeroToThousand(x):
	if x < 100:
		return zeroToHundred(x)
	lastTwoDigit = zeroToHundred(x%100)
	hundred = zeroToNine(x//100) + " hundred"
	result = hundred
	if lastTwoDigit != "":
		result += " and " + lastTwoDigit
	return result

def zeroToThousandInclusive(x):
	if x == 1000:
		return "one thousand"
	return zeroToThousand(x)

def stripNonLetters(str):
	return re.sub("[^a-zA-Z]","",str)

total = 0
for x in range(1,1001):
	text = zeroToThousandInclusive(x)
	stripped = stripNonLetters(text)
	length = len(stripped)
	total += length
	#print str(x) + ": " + text + " => " + stripped + "(" + str(length) + ")"

print(total)