
#program to check the normality of the features.

import scipy
from numpy import transpose

def normality_check(x_train):
	n=x_train.transpose()
	k=[0.0]*len(n)
	p=[0.0]*len(n)
	N=[1]*len(n) # array holding 1 or 0 values : 1-> it is normally distributed | --> it is not normally distributed
	alpha=1e-3
	for i in len(n):
		k[i], p[i] = scipy.stats.normaltest(n[i])
		if p[i] < alpha :
			N[i]=0
	return N