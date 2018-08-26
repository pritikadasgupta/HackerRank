# Geometric Distribution I

# The probability that a machine produces a defective product is 1/3. 
# What is the probability that the 1st defect is found during the 5th inspection?



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

#binomial probability mass function:
def geometricPDF(p,x):
	result = ((1-p)**(x-1))*p
	return result

if __name__ == '__main__':
	numerator, denominator = map(int, input().split()) #probability
	x = int(input()) #  inspection we want the probability of being the first defect for
	p = numerator/denominator

	# Defect found on the 5th inspection
	print("{:.3f}".format(geometricPDF(p,x)))

# 0.066
