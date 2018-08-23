#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def prime2(num):
	result = "Prime"
	if num % 2 == 0 or num <2: #even and 1
		result = "Not prime"  
	else: #odd numbers
		for i in range(3,num+1,2):
			if num % i == 0:
				if i > 1 and i !=num:
					result = "Not prime"
					break
	return result



def prime(num):
	result = "Prime"
	if num % 2 == 0 or num <2: #even and 1
		result = "Not prime"
	else: #odd numbers
		for i in range(1,num+1):
			if num % i == 0:
				if i > 1 and i !=num:
					result = "Not prime"
					break
	return result


# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  


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
# if __name__ == '__main__':
#     test_cases = int(input())

#     for i in range(0,test_cases):
# 	    num = int(input())
# 	    result = primes_sieve2(num)
# 	    if num in result:
# 	    	print("Prime")
# 	    else:
# 	    	print("Not prime")
# 	    print(result)
# if __name__ == '__main__':
#     test_cases = int(input())

#     for i in range(0,test_cases):
# 	    num = int(input())
# 	    result = prime2(num)
# 	    print(result)



if __name__ == '__main__':
    test_cases = int(input())

    for i in range(0,test_cases):
	    num = int(input())
	    result = is_prime(num)
	    if result:
	    	print("Prime")
	    else:
	    	print("Not prime")