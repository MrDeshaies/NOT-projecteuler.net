# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.

def fibonacci(limit):
    a,b = 0,1
    while True:
        yield b
        c = b+a
        a,b = b,c
        if b > limit:
            break

print(sum([i for i in fibonacci(4_000_000) if i%2 == 0]))