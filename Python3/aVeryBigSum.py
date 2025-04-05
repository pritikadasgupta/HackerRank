#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar: list[int]) -> int:
    """
    This is a functin to calculate the sum of a list of integers.

    Args:
        ar: A list of integers.

    Returns:
        The sum of the integers in the list.

    Raises:
        TypeError: If the input is not a list of integers.
    """
    if not isinstance(ar, list) or not all(isinstance(x, int) for x in ar):
        raise TypeError("Input must be a list of integers")
    return sum(ar)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        ar_count = int(input())
        ar = list(map(int, input().rstrip().split()))
        result = aVeryBigSum(ar)
        fptr.write(str(result) + '\n')
        fptr.close()
    except Exception as e:
        print(f"An error occurred: {e}")