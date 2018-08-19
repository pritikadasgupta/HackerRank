#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
	allSums = []
	for x in range(0,len(arr)-2): #row
		for y in range(0,len(arr[0])-2): #col
			myHourglass = [
			arr[x][y],
			arr[x][y+1],
			arr[x][y+2],
			arr[x+1][y+1],
			arr[x+2][y],
			arr[x+2][y+1],
			arr[x+2][y+2]]
			sumHourglass = sum(myHourglass)
			allSums.append(sumHourglass)
	return max(allSums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
