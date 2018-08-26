# Least Square Regression Line

# A group of five students enrolls in Statistics immediately after taking a Math aptitude test. 
# ch student's Math aptitude test score, x, and Statistics course grade, y, 
# can be expressed as the following list of (x,y) points:
# (95,85)
# (85,95)
# (80,70)
# (70,65)
# (60,70)

# If a student scored an 80 on the Math aptitude test, 
# what grade would we expect them to achieve in Statistics? 

# Determine the equation of the best-fit line using the least squares method, 
# then compute and print the value of y when x=80.

#!/bin/python3

import math

def mean(arr): #average
    myAverage = sum(arr) / float(len(arr))
    return myAverage

def leastSquares(x,y,n):
	meanx = mean(x)
	meany = mean(y)
	sum1 = 0
	sum2 = 0
	for i in range(0,n):
		sum1 = sum1 + ((x[i]-meanx)*(y[i]-meany))
		sum2 = sum2 + ((x[i]-meany)**2)
	slope = sum1/sum2
	yIntercept = meany - slope*meanx
	return [slope, yIntercept]

if __name__ == '__main__':
	x = []
	y = []
	for i in range(0,5):
		a,b = map(float, input().split()) # x,y points
		x.append(a)
		y.append(b)
	bestfit = leastSquares(x,y,5)
	result = 80*bestfit[0] + bestfit[1]
	print("{:.3f}".format(result))
	# 78.279