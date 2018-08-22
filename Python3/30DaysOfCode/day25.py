#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def prime(num):
	result = "Prime"
	if num % 2 == 0 or num <2: #even and 1
		result = "Not prime"
	else: #odd numbers
		# divisors=[]
		for i in range(1,num+1):
			if num % i == 0:
				# divisors.append(i)
				if i > 1 and i !=num:
					# print(i)
					result = "Not prime"
					break
	return result

if __name__ == '__main__':
    test_cases = int(input())

    for i in range(0,test_cases):
	    num = int(input())
	    result = prime(num)
	    print(result)