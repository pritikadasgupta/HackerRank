#!/bin/python3

import math
import os
import random
import re
import sys

def multiples(num):
    for x in range(1,11):
        print(str(num)+" x "+str(x)+" = "+str(num*x))

if __name__ == '__main__':
    n = int(input())
    multiples(n)
