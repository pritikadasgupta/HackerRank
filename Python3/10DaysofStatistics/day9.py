# Multiple Linear Regression

#!/bin/python3

import math
from sklearn import linear_model

if __name__ == '__main__':
	m, n = map(int, input().split()) #(the number of observed features) and  (the number of feature sets Andrea studied), respectively. 
	
	# Each of the n subsequent lines contain m+1 space-separated decimals; 
	# the first m elements are features (f1,f2,f3,...,fm), 
	# and the last element is the value of Y for the line's feature set.
	
	X = []
	Y = []
	for i in range(0,n):
	    x = [0]
	    elements = list(map(float, input().split()))
	    for j in range(0,len(elements)):
	        if j < m:
	            x.append(elements[j])
	        else:
	            Y.append(elements[j])
	    X.append(x)

	model = linear_model.LinearRegression()
	model.fit(X,Y)
	
	q = int(input()) #denoting the number of feature sets Andrea wants to query for. 


	new = [] 
	for i in range(q):
	    x = [0]
	    elements = list(map(float, input().split()))
	    for j in range(0,len(elements)):
	        x.append(elements[j])
	    new.append(x)

	
	result = model.predict(new)
	for i in range(len(result)):
	    print(round(result[i],2))

