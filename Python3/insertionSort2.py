#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort1(n, arr):
	store = arr[len(arr)-1]
	add = []
	for i in range(len(arr)-2,-1,-1):
		new = arr[0:i+1]
		if arr[i] > store and arr[i]!=arr[0]:
			add.insert(0,arr[i])
			new=new+add
		elif arr[i] <=store:
			add.insert(0,store)
			new = new+add
			break
		elif arr[i] == arr[0]:
			add.insert(0,arr[i])
			new=new+add
			new = arr[0:n-1]
			new.insert(0,store)
			break
	return new

def insertionSort2(n, arr):
	for i in range(2,n+1):
		arr1 = arr[0:i]
		arr2 = arr[i:n]
		newarr = insertionSort1(len(arr1),arr1)
		arr = newarr + arr2
		print(*arr, sep=' ')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
