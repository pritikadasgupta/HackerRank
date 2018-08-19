#!/bin/python3

import sys

def bubbleSort(n,a):
	numberOfSwaps_overall = 0
	for i in range(0,n):
		numberOfSwaps = 0
		for j in range(0,n-1):
			if a[j] > a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
				numberOfSwaps+=1
				numberOfSwaps_overall+=1
		if numberOfSwaps==0:
			break
	return numberOfSwaps_overall,a

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
num,new_a = bubbleSort(n,a)
print("Array is sorted in "+str(num)+" swaps.")
print("First Element: "+ str(new_a[0]))
print("Last Element: "+ str(new_a[len(new_a)-1]))