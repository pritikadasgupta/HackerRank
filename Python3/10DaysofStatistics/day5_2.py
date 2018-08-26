# Poisson Distribution II

# The manager of a industrial plant is planning to buy a machine of either type A or type B. 
# For each day’s operation:

# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
# The daily cost of operating A is CA = 160 + 40*(X^2).
# The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
# The daily cost of operating B is CB = 128 + 40*(Y^2).

# Assume that the repairs take a negligible amount of time and the machines are 
# maintained nightly to ensure that they operate like new at the start of each day. 
# Find and print the expected daily cost for each machine.


#!/bin/python3

import math

# Poisson distribution
# represents the number of events occurring in a fixed time interval with a rate parameters λ. 
# λ tells you the rate at which the number of events occur.  
# The average and variance is λ.
# E[X] = λ 
# E[X^2] = λ + λ^2

if __name__ == '__main__':
	λA,λB = map(float, input().split()) #A and B's mean
	cost_X = 160 + 40*(λA + λA**2)
	cost_Y = 128 + 40*(λB + λB**2)
	print("{:.3f}".format(cost_X))
	print("{:.3f}".format(cost_Y))
	# 226.176
	# 286.100
