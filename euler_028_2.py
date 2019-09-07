# heh... I found a much simpler solution. I'm so silly sometimes.
# the series is actually simple if you look at ALL the terms, and don't
# split it into unique diagonals...
GRID_SIZE = 1001
numberOfTerms = 2*(GRID_SIZE-1) + 1
terms = [1]
for i in range(0,numberOfTerms-1):
    terms.append(terms[-1] + (2*(i//4 + 1)))
print(sum(terms))