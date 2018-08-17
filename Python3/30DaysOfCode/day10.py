#!/bin/python3

import math
import os
import random
import re
import sys

def makeBinary(n):
	#convert to base 2
	binaryN = str(bin(n))

	#count number of consecutive 1s and save in list
	binaryList = list(binaryN)

	start = 0
	cons1List = []
	while start <len(binaryList):
		cons1 = 0
		for x in range(start,len(binaryList)):
			if binaryList[x]=='1':
				cons1 = cons1+1
			elif binaryList[x]=='b' or binaryList[x]=='0':
				break
		start = x+1
		cons1List.append(cons1)


	#find largest number
	#print base 10 integer corresponding to max number of consecutive 1s
	return(max(cons1List))

if __name__ == '__main__':
    n = int(input())
    print(makeBinary(n))
