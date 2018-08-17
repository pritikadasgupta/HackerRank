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
		myMedian = arr[midIndex]
	return myMedian

def mode(n,arr):
	dictofcounts = {}
	listofcounts = []
	for i in arr:
		countofi = arr.count(i) # count items for each item in list
		listofcounts.append(countofi) # add counts to list
		dictofcounts[i]=countofi # add counts and item in dict to get later
	maxcount = max(listofcounts) # get max count of items
	if maxcount ==1:
		myMode = min(arr) #all items occur once, so grab minimum of the arr
	else:
		modelist = [] # if more than one mode, add to list to print out
		for key, item in dictofcounts.items():
			if item ==maxcount: # get item from original list with most counts
				modelist.append(str(key))
		numbers = [ int(x) for x in modelist ]
		myMode = min(numbers)
	return myMode

if __name__ == '__main__':
    n = int(input())
	arr = list( map(int, input().split()) )
	print(mean(n,arr))
	print(median(n,arr))
	print(mode(n,arr))
