#!/bin/python3

import math
import os
import random
import re
import sys

def mean(n,arr):
    myAverage = sum(arr) / float(len(arr))
    return myAverage

def median(n, arr):
    arr.sort()
    #find two middle elements
    if n % 2 == 0:
        #average two middle elements
        midIndex1 = int(n/2)-1
        midIndex2 = midIndex1+1
        myMedian = mean(2,[arr[midIndex1],arr[midIndex2]])
    elif n % 2 !=0:
        midIndex = int(n/2)+(n%2>0)
        myMedian = arr[midIndex-1]
    return myMedian

def splitArray(n,arr):
	if n % 2 == 0:
		arr1 = arr[0:int(n/2)]
		arr2 = arr[int(n/2):n]
	elif n % 2 !=0:
		Q2 = median(n,arr)
		arr1 = arr[0:int(n/2)]
		arr2 = arr[int(n/2)+1:n]
	return [arr1,arr2]

def makeQuartiles(n,arr):
	Q2 = int(median(n,arr))
	arrays = splitArray(n,arr)
	Q1 = int(median(len(arrays[0]),arrays[0]))
	Q3 = int(median(len(arrays[1]),arrays[1]))
	return [Q1,Q2,Q3]

if __name__ == '__main__':
    n = int(input())
	arr = list( map(int, input().split()) )
	quartiles = makeQuartiles(n,arr)
	for i in range(0,3):
		print(quartiles[i])
