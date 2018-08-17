#!/bin/python3

import math
import os
import random
import re
import sys

def reverseIt(n, arr):
    newList = []
    for x in range(0,n):
        y=n-x-1
        newList.append(arr[y])
    return(newList)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    myList = reverseIt(n,arr)
    print(*myList, sep=' ')