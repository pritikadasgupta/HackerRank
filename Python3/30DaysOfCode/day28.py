#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    firstName = []
    # emailID = []
    isGmail = re.compile("^[a-z\.]+@gmail.com$")
	accounts = dict()
    for N_itr in range(N):
        firstNameEmailID = input().split()
        # firstName.append() = firstNameEmailID[0]
        # emailID.append() = firstNameEmailID[1]
		if isGmail.match(firstNameEmailID[1]):
			accounts[firstNameEmailID[1]] = firstNameEmailID[0]
	sorted_names = sorted(accounts.values())
	print(*sorted_names, sep="\n")
