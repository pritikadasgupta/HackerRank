#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, n, d):
	for i in range(0,d):
		a.append(a[0])
		a.pop(0)
	return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, n, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
