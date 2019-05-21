#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
	n=len(arr)
	if n==1:
		return arr[0]
	elif n==2:
		return max(arr)
	else:
		return max(arr[0],arr[0] + maxSubsetSum(arr[2:]),maxSubsetSum(arr[1:]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(n,arr)

    fptr.write(str(res) + '\n')

    fptr.close()
