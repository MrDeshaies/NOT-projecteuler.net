# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
# so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its alphabetical position and 
# adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?

import re

def load_words(filename):
    f = open(filename, "r")
    data = f.readline()
    f.close()

    # file looks like "BOB","MARY","JANE"
    # split will keep an empty token at the front and end. Get rid of them
    words = re.split(r'\W+',data)
    words = words[1:len(words)-1]
    return words

def compute_score(word):
    A = ord("A")
    return sum(ord(x.upper()) - A + 1 for x in word)

def generate_triangle(upper_limit):
    triangle_numbers = []
    i = 1
    while True:
        n = int((i * (i+1)) / 2)
        triangle_numbers.append(n)
        i += 1
        if n > upper_limit:
            break
    return triangle_numbers

# compute the score for each word
words = load_words("p042_words.txt")
word_scores = [compute_score(x) for x in words]
# find the relevant triangle numbers
triangle_numbers = generate_triangle(max(word_scores))
# count how many words have a triangle score...
print(len([x for x in word_scores if x in triangle_numbers]))