# Normal Distribution I

# In a certain plant, the time taken to assemble a car is a random variable, X, 
# having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
# What is the probability that a car can be assembled at this plant in:

# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

#!/bin/python3

import math
from scipy.stats import norm

# Normal distribution
# continuous distribution or a function that can take on values anywhere on the real line
# The normal distribution is parameterized by two parameters: the mean of the distribution μ and the variance σ2.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# #normal function (this works for PDF only)
# def normal(mean,variance,x):
# 	a = 1
# 	b = (2*math.pi*variance)**0.5
# 	c = (x - mean)**2
# 	d = 2*variance
# 	result = (a/b)*math.exp(-c/d)
# 	# result = (1/((2*math.pi*variance)**0.5))*math.exp(-((x-mean)**2)/(2*variance))
# 	return result

if __name__ == '__main__':
	mean, std = map(float, input().split()) #mean and std of X
	a = float(input()) #  for question 1
	l, u = map(float, input().split()) #lower and upper range (for question 2)

	result = norm.cdf(a,mean,std)

	print("{:.3f}".format(result))
	# 0.401

	result = norm.cdf(u,mean,std) - norm.cdf(l,mean,std)
	print("{:.3f}".format(result))
	# 0.341
