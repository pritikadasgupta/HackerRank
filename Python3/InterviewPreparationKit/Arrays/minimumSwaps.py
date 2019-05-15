#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	# initialize number of swaps
	numSwaps = 0
	# find lowest element
	arrMin = min(arr)

	for i in range(0,len(arr)-1):
		pointer = arr.index(arrMin)
		if arr[i]!=arr[pointer]:
			arr[i], arr[pointer] = arr[pointer], arr[i] 
			numSwaps+=1
		arrMin+=1
	return numSwaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
