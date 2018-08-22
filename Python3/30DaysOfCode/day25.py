#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def prime(num):
	if num ==1:
		result = "Not prime"
	else:
		divisors=[]
		for i in range(1,num+1):
			if num % i == 0:
				divisors.append(i)
		prime_divisors = [1,num]
		for j in range(0,len(prime_divisors)):
			if 	divisors[j]==prime_divisors[j]:
				result = "Prime"
			else:
				result = "Not prime"
	return result

if __name__ == '__main__':
    test_cases = int(input())

    for i in range(0,test_cases):
	    num = int(input())
	    result = prime(num)
	    print(result)