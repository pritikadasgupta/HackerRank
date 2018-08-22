#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def prime(num):
	if num % :
		result = "Prime"
	else
		result = "Not Prime"
	return result

if __name__ == '__main__':
    test_cases = int(input())

    for i in range(0,test_cases):
	    num = int(input())
	    result = prime(num)
	    print(result)
