#!/bin/python3

import math
import os
import random
import re
import sys

class SplitString:
	def __init__(self,mystring):
		self.mystring = mystring
	def even(self):
		newstring=""
		for x in range(0,len(self.mystring)):
			if x % 2 ==0:
				newstring = newstring+mystring[x]
		return(newstring)
	def odd(self):
		newstring=""
		for x in range(0,len(self.mystring)):
			if x % 2 !=0:
				newstring = newstring+mystring[x]
		return(newstring)


t = int(input())
for i in range(0, t):
    mystring = str(input()) 
    p = SplitString(mystring)  
    print(p.even()+" "+p.odd())