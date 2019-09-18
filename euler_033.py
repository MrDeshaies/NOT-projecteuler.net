from fractions import Fraction

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
# may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

result = Fraction(1,1)

def get_digit(num,pos):
    return int(str(num)[pos])

def test_match(num,deno):
    global result
    new_fraction = Fraction(get_digit(num,0), get_digit(deno,1))
    if new_fraction == Fraction(num,deno):
        print("Match: " + str(num) + " / " + str(deno))
        result *= new_fraction

def find_matching_fractions():
    for tens in range(1,10):
        for unit in range(1,10):
            if unit == tens: # skip 88/88, for example
                continue
            numerator = tens * 10 + unit
            # find a denominator. The tens need to be the unit
            for i in range(1,10):
                denominator = unit * 10 + i
                test_match(numerator,denominator)

find_matching_fractions()
print("Denominator of product of matching fractions: " + str(result.denominator))