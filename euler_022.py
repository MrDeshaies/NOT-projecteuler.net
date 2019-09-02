import re

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

def nameValue(name):
    sum = 0
    for c in name.upper():
        sum += ord(c)-ord('A')+1 # +1 so that A is 1, not 0
    return sum


f = open("p022_names.txt", "r")
data = f.readline()
f.close()

# file looks like "BOB","MARY","JANE"
# split will keep an empty token at the front and end. Pop the end-one,
# but keep the leading one so the list starts at 1, lolz.
names = re.split(r'\W+',data)
names.pop()
names.sort()

total = 0
i = 0
for name in names:
    total += nameValue(name) * i
    i += 1

print("Colin: " + str(nameValue("COLIN")))
print(total)
