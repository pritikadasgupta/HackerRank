#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
	n=0
	p=0
	z=0
	length= len(arr)
	for i in range(0,len(arr)):
		if arr[i]<0: #neg
			n +=1
		elif arr[i]>0: #pos
			p +=1
		elif arr[i] == 0: #zero
			z +=1
	print(format(p/len(arr),'.6f'))
	print(format(n/len(arr),'.6f'))
	print(format(z/len(arr),'.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
