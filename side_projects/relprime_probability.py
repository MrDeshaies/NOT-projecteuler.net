# Ben Bartlett @bencbartlett
# Mar 15, 2021
# https://twitter.com/bencbartlett/status/1371579739215855620
# the probability that two randomly-chosen integers are relatively prime is exactly 6/π²

import random
from math import gcd,pi

target_ratio = 6 / pi**2
num_iterations = 1_000_000
max_number = 100_000_000
relprime_counts = {True:0, False:0}

def are_relprime(x,y):
    return gcd(x,y) == 1

i = 0
while i < num_iterations:
    i += 1
    x,y = random.randint(2,max_number), random.randint(2,max_number)
    relprime = are_relprime(x,y)
    relprime_counts[relprime] += 1

actual_ratio = relprime_counts[True] / num_iterations
percent_difference = abs(actual_ratio - target_ratio) / target_ratio * 100
print(relprime_counts)
print("Target ratio: {:.5f}\nActual ratio: {:.5f}\nDifference  : {:.5f} %".format(
    target_ratio, actual_ratio, percent_difference))