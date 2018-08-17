#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
	# size of the matrix
	n = len(arr)

	# sum of first diagonal
	d1 = sum(arr[i][i] for i in range(n))

	# sum of second diagonal
	d2 = sum(arr[i][n-i-1] for i in range(n))

	# absolute difference of sums
	return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
