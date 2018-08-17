#!/bin/python3

import math
import os
import random
import re
import sys

class makePhone:
	def __init__(self,mystring):
		self.mystring = mystring
	def make(self):
		return dict([
			(self.mystring[0],self.mystring[1])
			])

class lookUp:
	def __init__(self,entry,phoneBook):
		self.phoneBook = phoneBook
		self.entry = entry
	def look(self):
		if self.entry in self.phoneBook:
			return(self.entry+"="+self.phoneBook[self.entry])
		else:
			return("Not found")



nEntry = int(input())
orig = dict()
for i in range(0, nEntry):
	myEntry = list(map(str, input().rstrip().split()))
	p = makePhone(myEntry)
	orig.update(p.make())

for line in sys.stdin:
	if line == "":
		break
	else:
		f = lookUp(line,orig)
		print(f.look())

# EOF error

# entryToLookUp = str(input())
# while entryToLookUp !="":
# 	f = lookUp(entryToLookUp,orig)
# 	print(f.look())
# 	entryToLookUp = str(input())
