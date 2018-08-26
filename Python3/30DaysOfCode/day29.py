#!/bin/python3

import math
import os
import random
import re
import sys

def bitwise(n,k):
	result = 0
    for j in range(1, n):
        for i in range(j + 1, n + 1):
            pointer = j & i
            if k > pointer > result:
                result = pointer
    return result


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print(bitwise(n,k))