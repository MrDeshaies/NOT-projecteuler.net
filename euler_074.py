# Euler 74
# The number 145 is well known for the property that the sum of the factorial 
# of its digits is equal to 145:
#
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# 
# Perhaps less well known is 169, in that it produces the longest chain of 
# numbers that link back to 169; it turns out that there are only three such 
# loops that exist:
#
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
#
# It is not difficult to prove that EVERY starting number will eventually get 
# stuck in a loop. For example,
#
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the 
# longest non-repeating chain with a starting number below one million is 
# sixty terms.
# 
# How many chains, with a starting number below one million, contain exactly
# sixty non-repeating terms?

from math import factorial
import multiprocessing as mp

DESIRED_CHAIN_LENGTH = 60

DIGIT_FACTORIAL = [factorial(i) for i in range(10)]
def sum_digits_factorial(x):
    return sum([DIGIT_FACTORIAL[int(c)] for c in str(x)])

def chain_length(x):
    seen = [x]
    while True:
        s = sum_digits_factorial(x)
        if s in seen:
            return len(seen)
        seen.append(s)
        x = s

def sum_chain_lengths(numbers):
    return sum([1 for x in numbers if chain_length(x) == DESIRED_CHAIN_LENGTH])

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

small_sums = []
def collect_result(result):
    global small_sums
    small_sums.append(result)

if __name__ == '__main__':
    #Single threaded version:
    # print(sum([1 for x in range(1_000_000) if chain_length(x) == DESIRED_LENGTH]))

    # parallelize the processing...
    print("Paralellizing across {} processors".format(mp.cpu_count()))
    max_number = 1_000_000
    chunk_size = max_number // mp.cpu_count()
    numbers_in_chunks = list(chunks(list(range(max_number)),chunk_size))
    pool = mp.Pool(mp.cpu_count())
    [pool.apply_async(sum_chain_lengths, args=(numbers, ), callback=collect_result) for numbers in numbers_in_chunks]
    pool.close()
    pool.join()

    print(small_sums)
    print(sum(small_sums))
