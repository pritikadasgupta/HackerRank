# Pearson Correlation Coefficient I

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


def pearson(X,Y,n):
	meanx = mean(X)
	meany = mean(Y)
	sum1 = 0
	for i in range(0,n):
		sum1 = sum1 + ((X[i]-meanx)*(Y[i]-meany))
	return sum1/(n*std(X)*std(Y))

if __name__ == '__main__':
	n = int(input()) #  n
	X = list(map(float, input().split())) # set X
	Y = list(map(float, input().split())) # set X	
	print("{:.3f}".format(pearson(X,Y,n)))
	# 0.612