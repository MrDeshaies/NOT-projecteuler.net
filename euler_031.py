# In England the currency is made up of pound, £, and pence, p, 
# and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

COIN_VALUES = [200, 100, 50, 20, 10, 5, 2, 1]
total_count = 0

def find(sum,index):
    global total_count
    """Find how many ways to make change for 'sum' starting at 'COIN_VALUES[index]'"""
    if index >= len(COIN_VALUES) or sum == 0:
        return
    
    coin_value = COIN_VALUES[index]

    # we've reached the pence; only one way to make change
    if sum != 0 and coin_value == 1:
        total_count += 1
        return
    
    if coin_value > sum:
        # recurse with next smaller coins
        find(sum,index+1)
        return
    
    # otherwise iterate and recurse
    for i in range(0, sum//coin_value + 1):
        remainder = sum - (coin_value * i)
        if remainder == 0:
            total_count += 1
        else:
            find(remainder, index+1)

find(200,0)
print("Total ways " + str(total_count))