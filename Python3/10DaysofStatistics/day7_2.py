# Spearman's Rank Correlation Coefficient

#!/bin/python3

import math

def ranks(arr,n):
	seq = sorted(arr)
	index = [seq.index(i)+1 for i in arr]
	return index

def di2(X,Y,n):
	rankx = ranks(X,n)
	ranky = ranks(Y,n)
	sum_di2 = 0
	for i in range(0,n):
		sum_di2 = sum_di2 + ((rankx[i]-ranky[i])**2)
	return sum_di2

def spearman(X,Y,n):
	return (1 - (6*di2(X,Y,n))/(n*((n**2)-1)))

if __name__ == '__main__':
	n = int(input()) #  n
	X = list(map(float, input().split())) # set X
	Y = list(map(float, input().split())) # set Y	
	print("{:.3f}".format(spearman(X,Y,n)))
	# 