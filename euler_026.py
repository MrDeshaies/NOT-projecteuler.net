# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
# denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import math

class UnitDivision:
    def __init__(self,divisor):
        self.term = 10
        self.divisor = divisor
        self.answer = []
    
    def borrow(self):
        self.term *= 10
        self.answer.append(0)
    
    def divide(self):
        while self.term != 0:
            while self.term < self.divisor:
                self.borrow()
            f = math.floor(self.term/self.divisor)
            self.term = self.term - (self.divisor * f)
            self.term *= 10
            self.answer.append(f)
    
    def printAnswer(self):
        print("0." + str("".join([str(x) for x in self.answer])))

x = UnitDivision(8)
x.divide()
x.printAnswer()
