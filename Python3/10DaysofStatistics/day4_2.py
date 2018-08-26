# Binomial Distribution II

# A manufacturer of metal pistons finds that, on average, 
# 12% of the pistons they manufacture are rejected 
# because they are incorrectly sized. 

# What is the probability that a batch of 10 pistons will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?


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
	p1,n = map(int, input().split()) 
	# p1 = percentage of defective pistons -- p = p(rejects)
	p = p1/100
	# n = size of the current batch of pistons -- this is the number of trials

	# 1. No more than 2 rejects?
	myp = 0
	for x in range(0,3):
		myp = myp + binomialPMF(n,p,x)
	print("{:.3f}".format(myp))

	# 2. At least 2 rejects?
	myp = 0
	for x in range(2,n+1):
		myp = myp + binomialPMF(n,p,x)
	print("{:.3f}".format(myp))

# 0.891
# 0.342
