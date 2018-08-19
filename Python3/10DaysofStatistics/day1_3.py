#!/bin/python3

import math
import os
import random
import re
import sys

def mean(n,arr):
    myAverage = sum(arr) / float(len(arr))
    return myAverage

def squaredDistance(n, arr):
	avg = mean(n,arr)
	sqrd = []
	for i in range(0,n):
		sqrd.append((arr[i]-avg)*(arr[i]-avg))
	return sqrd

if __name__ == '__main__':
    n = int(input())
	arr = list( map(int, input().split()) )
	10 40 30 50 20
	result = math.sqrt(sum(squaredDistance(n,arr))/n)
	print(str.format('{0:.1f}', result))

