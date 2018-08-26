# Central Limit Theorem III

# You have a sample of 100 values from a population with mean 500 and with standard deviation 80. 
# Compute the interval that covers the middle 95% of the distribution of the sample mean; 
# in other words, compute A and B such that P(A<x<B)=0.95. 
# Use the value of z=1.96. Note that z is the z-score.

#!/bin/python3

import math

def pnorm(x, mean, std):
    return (0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5)))))

if __name__ == '__main__':
	a = float(input()) #  sample size
	b = float(input()) #  mean
	c = float(input()) #  std
	d = float(input()) #  distribution percentage (as a decimal)
	e = float(input()) #  z score

	result = b - e*c/math.sqrt(a)
	print("{:.2f}".format(result))
	# 484.32

	result = b + e*c/math.sqrt(a)
	print("{:.2f}".format(result))
	# 515.68
