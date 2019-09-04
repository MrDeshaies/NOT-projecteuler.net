# Fibonacci sequence goes like F1 = 1, F2 = 1, F3 = 2, F4 = 3 ... F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a = 1
b = 1
seq = 3
maxLength = 0
while True:
    # generate the next one
    c = a + b
    a = b
    b = c

    length = len(str(c))
    if length > maxLength:
        maxLength = length
        if maxLength % 100 == 0:
            print("seq " + str(seq) + " has length " + str(length))

    seq += 1
    if length == 1000:
        break