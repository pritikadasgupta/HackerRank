# Binomial Distribution I

# The ratio of boys to girls for babies born in Russia is 1.09:1. 
# If there is 1 child born per birth, 
# what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. 
# Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

#!/bin/python3

import math
import os
import random
import re
import sys


# Binomial distribution has a random variable, X
# X = number of successes in a sequence of n binary trials
# each trial has success probability, p

# the expectation of X, or the mean of X
# E(X) = n*p

# the variance of X
# Var(X) = n*p*(1-p)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#binomial probability mass function:
def binomialPMF(n,p,x):
	n_choose_x = factorial(n)/(factorial(x)*factorial(n-x))
	result = n_choose_x*(p**x)*((1-p)**(n-x))
	return result

if __name__ == '__main__':
	a,b = map(float, input().split())

	n = 6 # 6 children, 6 binary trials
	p = a/(a+b) # p = p(boy)
	myp = 0

	for x in range(3,n+1):
		myp = myp + binomialPMF(n,p,x)

	print("{:.3f}".format(myp))
