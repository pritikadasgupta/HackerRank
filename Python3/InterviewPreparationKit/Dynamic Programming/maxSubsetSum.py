#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
	maxVal = [arr[0],max(arr[:2])]
	for i in arr[2:]:
		maxVal.append(max(
			maxVal[-2]+i,i,maxVal[-1]
			))
	return maxVal[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
