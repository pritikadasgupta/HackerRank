#!/bin/python3

import math
import os
import random
import re
import sys


def weird(num):
	string1 = "Weird"
	string2 = "Not Weird"
	if num % 2 != 0: #odd
    		return(string1)
	elif (num % 2 == 0 and num >=2 and num <=5):
			return(string2)
	elif (num % 2 == 0 and num >=6 and num <=20):
			return(string1)
	elif (num % 2 == 0 and num >=20):
			return(string2)

if __name__ == '__main__':
    n = int(input())
    print(weird(n))