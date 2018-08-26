# Geometric Distribution II

# The probability that a machine produces a defective product is 1/3. 
# What is the probability that the 1st defect is found during the first 5 inspections?


#!/bin/python3

import math
import os
import random
import re
import sys


# Geometric distribution
# number of failures before you get a success in a series of Bernoulli trials
# X = number of trials before first success 
# each trial has success probability, p

# the expectation of X, or the mean of X
# E(X) = (1-p)/p

# the variance of X
# Var(X) = (1-p)/(p^2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#geometric probability mass function:
def geometricPDF(p,x):
	result = ((1-p)**(x-1))*p
	return result

if __name__ == '__main__':
	numerator, denominator = map(int, input().split()) #probability
	n = int(input()) #  inspection we want the probability of being the first defect being discovered by
	p = numerator/denominator

	# Defect found on any of the first 5 inspection
	result = 0
	for x in range(1,n+1):
		result = result + geometricPDF(p,x)
	print("{:.3f}".format(result))
	# 0.868
