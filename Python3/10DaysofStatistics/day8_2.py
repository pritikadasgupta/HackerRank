# Pearson Correlation Coefficient II

#!/bin/python3

import math

def mean(arr): #average
    myAverage = sum(arr) / float(len(arr))
    return myAverage

def ss(arr): #sum of square deviations
    a = mean(arr)
    ss = sum((x-a)**2 for x in arr)
    return ss

def std(arr): #standard deviation
	n = len(arr)
	return (ss(arr)/(n))**0.5


if __name__ == '__main__':
	n = 100000
	Y = []
	X = []
	for i in range(0,n):
		Y.append(((-3*i) - 8)/4)
		X.append(((-3*i) - 7)/4)
	b1 = -3/4
	b2 = -3/4
	stdx = std(X)
	stdy = std(Y)
	p = (b1*b2)**0.5

	print("{:.2f}".format(-p))
	# -0.75