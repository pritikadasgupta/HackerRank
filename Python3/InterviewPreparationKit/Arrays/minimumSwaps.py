#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(n,arr):
	# initialize number of swaps
	numSwaps = 0
	for i in range(0,n-1):
		while arr[i] !=i+1:
			pointer = arr[arr[i] - 1]
			arr[arr[i] - 1],arr[i] = arr[i],pointer
			numSwaps+=1
	return numSwaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(n,arr)

    fptr.write(str(res) + '\n')

    fptr.close()
