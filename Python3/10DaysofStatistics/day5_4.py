# Normal Distribution II

# The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10. 
# If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

# 1. Scored higher than 80 (i.e., have a grade > 80)?
# 2. Passed the test (i.e., have a grade >= 60)?
# 3. Failed the test (i.e., have a grade < 60)?
# Find and print the answer to each question on a new line, 
# rounded to a scale of 2 decimal places.

#!/bin/python3

import math

# Normal distribution
# continuous distribution or a function that can take on values anywhere on the real line
# The normal distribution is parameterized by two parameters: the mean of the distribution μ and the variance σ2.

# 70 10
# 80
# 60

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
	b = float(input()) #  for question 2 and 3

	cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

	result = 100*(1 - cdf(a))
	print("{:.2f}".format(result))
	# 15.87

	result = 100*(1 - cdf(b))
	print("{:.2f}".format(result))
	# 84.13

	result = 100*cdf(b)
	print("{:.2f}".format(result))
	# 15.87
