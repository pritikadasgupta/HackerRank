#!/bin/python3

import math
import os
import random
import re
import sys
# import datetime

# Complete the solve function below.
def fine(dayR, monthR, yearR, dayD, monthD, yearD):
  if yearR > yearD: #book returned after calendar year in which it was expected
    result = 10000
  elif yearR == yearD: #within same calendar year
    if monthR > monthD: #but after expected month
      result = 500*(monthR - monthD)
    if monthR == monthD: #within same month
      if dayR == dayD or dayR < dayD: #on or before due day
        result = 0
      else:
        result = 15*(dayR - dayD) #after expected day
    if monthR < monthD:
      result = 0
  elif yearR < yearD:
    result = 0
  return str(result)

if __name__ == '__main__':
  date_returned = input('')
  date_due = input('')
  dayR, monthR, yearR = map(int, date_returned.split(' '))
  dayD, monthD, yearD = map(int, date_due.split(' '))
  # date1 = datetime.date(year, month, day)
  print(fine(dayR, monthR, yearR, dayD, monthD, yearD))


#test cases
# 2 6 2014
# 5 7 2014

# 31 12 2009
# 1 1 2010

# 1 1 1
# 8 8 8