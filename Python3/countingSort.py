#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
	n = len(arr)
	arrMin = min(arr)
	arrMax = max(arr)
	countingArray = []
	for i in range(arrMin, arrMax+1):
		countingArray.append(arr.count(i))
	sortedArray = []
	counter = 0
	for j in range(arrMin, arrMax+1):
		for k in range(0,countingArray[counter]):
			sortedArray.append(j)
		counter += 1
	return sortedArray


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
