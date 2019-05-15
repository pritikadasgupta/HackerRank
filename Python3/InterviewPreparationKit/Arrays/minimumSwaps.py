#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr, pos1, pos2): 
	arr[pos1], arr[pos2] = arr[pos2], arr[pos1] 
	return arr

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	# initialize number of swaps
	numSwaps = 0
	#sort array
	sortarr = sorted(arr)
	# find lowest element
	arrMin = min(arr)
	#start with 0 position
	i=0
	while (arr!=sortarr):
		pointer = arr.index(arrMin)
		if arr[i]!=arr[pointer]:
			swap(arr,i,pointer)
			numSwaps+=1
		arrMin+=1
		i+=1
	return numSwaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
