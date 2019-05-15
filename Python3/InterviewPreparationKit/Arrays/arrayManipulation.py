#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for i in range(0,len(queries)):
        a,b,c = queries[i][0],queries[i][1],queries[i][2]
        arr[a-1]+=c
        if((b)<=len(arr)): 
            arr[b] -= c;
    max = 0
    a = 0
    for j in arr:
        a+=j
        if max<a:
            max=a
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
