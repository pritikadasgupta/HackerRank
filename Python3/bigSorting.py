#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
# def bigSorting(unsorted):
#     sorted = [ int(x) for x in unsorted ]
#     sorted.sort()
#     sorted = [ str(x) for x in sorted ]
#     return sorted

def bigSorting(unsorted):
    return sorted(unsorted, key=int)

if __name__ == '__main__':
    n = int(input())
    unsorted = []

for _ in range(n):
    # unsorted_item = input()
    unsorted.append(input())
result = bigSorting(unsorted)
for s in result:
    print(s)

