# Poisson Distribution I

# A random variable, X, follows Poisson distribution with mean of 2.5. 
# Find the probability with which the random variable X is equal to 5.

#!/bin/python3

import math

# Poisson distribution
# represents the number of events occurring in a fixed time interval with a rate parameters λ. 
# λ tells you the rate at which the number of events occur.  
# The average and variance is λ.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#poisson function:
def poisson(λ,k):
	result = ((λ**k)*math.exp(-λ))/factorial(k)
	return result

if __name__ == '__main__':
	λ = float(input()) #X's mean = λ
	k = int(input()) #  value we want the probability for

	print("{:.3f}".format(poisson(λ,k)))
	# 0.067
