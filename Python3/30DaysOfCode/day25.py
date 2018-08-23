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
	elif num % 5 ==0:
		result = "Not prime"
	else: #odd numbers
		for i in range(1,num+1):
			if num % i == 0:
				if i > 1 and i !=num:
					result = "Not prime"
					break
	return result

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False #0 and 1 are not prime
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

# list = primes_sieve(12)
# for i in list:
# 	print(i)

def primes_sieve2(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*i, limitn, i):
            not_prime[f] = True
        primes.append(i)
    return primes


if __name__ == '__main__':
    test_cases = int(input())

    for i in range(0,test_cases):
	    num = int(input())
	    result = primes_sieve2(num)
	    if num in result:
	    	print("Prime")
	    else:
	    	print("Not prime")
	    print(result)