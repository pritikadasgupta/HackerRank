#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
# Instead of storing the actual values in the array, you store the difference between the current element and the previous element. So you add sum to a[p] showing that a[p] is greater than its previous element by sum. You subtract sum from a[q+1] to show that a[q+1] is less than a[q] by sum (since a[q] was the last element that was added to sum). By the end of all this, you have an array that shows the difference between every successive element. By adding all the positive differences, you get the value of the maximum element
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
