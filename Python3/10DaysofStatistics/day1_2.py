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

def freqArray(n,arr1,arr2):
	new_arr = []
	for i in range(0,n):
		for j in range(0,arr2[i]):
			new_arr.append(arr1[i])
	return new_arr

if __name__ == '__main__':
    n = int(input())
	arrX = list( map(int, input().split()) )
	arrF = list( map(int, input().split()) )
	new_arr = freqArray(n,arrX,arrF)
	quartiles = makeQuartiles(len(new_arr),new_arr)
	print(str.format('{0:.1f}', quartiles[2]-quartiles[0]))
