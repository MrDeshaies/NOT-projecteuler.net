# Euler 089
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
# Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way 
# of writing a particular number.
#
# For example, it would appear that there are at least six ways of writing the number sixteen:
#
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
#
# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the 
# most efficient, as it uses the least number of numerals.
#
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written 
# in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for 
# this problem.
#
# Find the number of characters saved by writing each of these in their minimal form.
#
# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
from math import floor

def read_file(filename):
    numerals = []
    f = open(filename, "r")
    for line in f:
        numerals.append(line.strip())
    f.close()
    return numerals

def num_to_roman(n):
    UNITS = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    TENS = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    HUNDS = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']

    unit,ten,hun,thou='','','',''
    if n >= 1000:
        x = floor(n/1000)
        thou = "M" * x
        n -= x*1000
    
    if n >= 100:
        x = floor(n/100)
        hun = HUNDS[x]
        n -= x*100

    if n >= 10:
        x = floor(n/10)
        ten = TENS[x]
        n -= x*10
    
    unit = UNITS[n%10]
    
    return thou+hun+ten+unit

def parse_roman(roman):
    VALUES = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    SUBSTITUTIONS = { "IV":"IIII", "IX":"IIIIIIIII", "XL":"XXXX", "XC":"XXXXXXXXX",
        "CD":"CCCC", "CM":"CCCCCCCCC"}
    
    for subs,exp in SUBSTITUTIONS.items():
        roman = roman.replace(subs,exp)
    
    value = 0
    for i in roman:
        value += VALUES[i]
    return value

def solve_089():
    saved = 0
    entries = read_file("p089_roman.txt")
    for i in entries:
        decimal = parse_roman(i)
        saved += len(i) - len(num_to_roman(decimal))
    print("We could save {} characters".format(saved))

if __name__ == '__main__':
    solve_089()