#!/bin/python3

import math
import os
import random
import re
import sys

def weightedMean(n,arrX,arrY):
	sum1=0
	sum2=0
	for i in range(0,n):
		sum1+=arrX[i]*arrY[i]
		sum2+=arrY[i]
	print(str.format('{0:.1f}', sum1/sum2))
if __name__ == '__main__':
	n = int(input())
	arrX = list( map(int, input().split()) )
	arrY = list( map(int, input().split()) )
	weightedMean(n,arrX,arrY)
