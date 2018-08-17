#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
	store = arr[len(arr)-1]
	add = []
	for i in range(len(arr)-2,-1,-1):
		new = arr[0:i+1]
		if arr[i] > store and arr[i]!=arr[0]:
			add.insert(0,arr[i])
			new=new+add
			print(*new, sep=' ')
		elif arr[i] <=store:
			add.insert(0,store)
			new = new+add
			print(*new, sep=' ')
			break
		elif arr[i] == arr[0]:
			add.insert(0,arr[i])
			new=new+add
			print(*new, sep=' ')
			new = arr[0:n-1]
			new.insert(0,store)
			print(*new, sep=' ')
			break


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
