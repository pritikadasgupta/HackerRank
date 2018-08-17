#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.

def runningTime(l):
	shifts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        compare = l[j]
        while (j >= 0) and (compare > key):
            l[j]=key
            l[j+1] = compare
            j -= 1
            if j >=0:
                compare = l[j]
            shifts +=1
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
