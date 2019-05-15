#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(n,q):
	q=[j-1 for j in q]
	numBribes=0
	p=list(range(0,n))
	for i,j in enumerate(q):
		if j-i>2:
			print("Too chaotic")
			return
		for k in range(max(j-1,0),i):
			if q[k] > j:
				numBribes+=1
	print(numBribes)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(n,q)
