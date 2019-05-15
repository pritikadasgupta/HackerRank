#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(n,q):
	# 1 cannot bribe (position 0, position 1)
	# 2 can only bribe once (position 0 and 1)
	# other positions can bribe once or twice (position x, x-1, x-2)
	i=n
	numBribes=0
	p=list(range(1,n+1))
	while (i>-1):
		if q[i-1]==p[i-1]: 
			i=i-1
		elif q[i-2]==p[i-1]:
			numBribes+=1
			# p[i-1],p[i-2]=p[i-2],p[i-1]
			i=i-1
		elif q[i-3]==p[i-1]:
			numBribes+=2
			# p[i-1],p[i-2]=p[i-2],p[i-1]
			# p[i-2],p[i-3]=p[i-3],p[i-2]
			i=i-1
		elif q[i-4]==p[i-1]:
			print("Too chaotic")
			return
		else:
			i=i-1
	print(numBribes)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(n,q)
