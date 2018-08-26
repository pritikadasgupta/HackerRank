# Central Limit Theorem II

# The number of tickets purchased by each student for the 
# University X vs. University Y football game follows a distribution that 
# has a mean of 2.4 and a standard deviation of 2.0.

# A few hours before the game starts, 100 eager students line up to purchase 
# last-minute tickets. If there are only 250 tickets left, 
# what is the probability that all 100 students will be able to purchase tickets?

#!/bin/python3

import math

def pnorm(x, mean, std):
    return (0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5)))))

if __name__ == '__main__':
	a = float(input()) #  number of last-minute tickets available at the box office
	b = float(input()) #  number of students waiting to buy tickets
	c = float(input()) #  mean number of purchased tickets
	d = float(input()) #  standard deviation

	result = pnorm(a, b * c, math.sqrt(b) * d)
	print("{:.4f}".format(result))
	# 0.6915
