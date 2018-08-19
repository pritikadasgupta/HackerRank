# In a single toss of 2 fair (evenly-weighted) six-sided dice, 
# find the probability that their sum will be at most 9.

import random

#single toss
min = 1
max = 6
dice1 = random.randint(min,max)
dice2 = random.randint(min,max)

# https://codereview.stackexchange.com/questions/114584/printing-all-possible-sums-of-two-n-sided-dice-rolls
def sumsFromTwoRolls(sides):
    return sorted(a + b for a in range(1, sides + 1) for b in range(1, sides + 1))

#probability that the sum will be at most 9
l = sumsFromTwoRolls(6)
numerator = sum(i <=9 for i in l)
denominator = len(l)

from fractions import Fraction
Fraction(numerator, denominator)

print(numerator/denominator)