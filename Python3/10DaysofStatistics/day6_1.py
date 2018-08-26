# Central Limit Theorem I

# A large elevator can transport a maximum of 9800 pounds. 
# Suppose a load of cargo containing 49 boxes must be transported via the elevator. 
# The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. 
# Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

#!/bin/python3

import math

def pnorm(x, mean, std):
    return (0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5)))))

if __name__ == '__main__':
	a = float(input()) #  maximum weight the elevator can transport
	b = float(input()) #  number of boxes in the cargo
	c = float(input()) #  mean weight of a cargo box
	d = float(input()) #  standard deviation of cargo box

	result = pnorm(a, b * c, math.sqrt(b) * d)
	print("{:.4f}".format(result))
	# 0.0098
