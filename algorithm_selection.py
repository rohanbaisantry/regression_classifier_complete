
# Program to check if the problem is a Classification or Regression problem
# using the type of target function in the SK-Learn library
# http://scikit-learn.org/dev/modules/generated/sklearn.utils.multiclass.type_of_target.html

from sklearn.utils.multiclass import type_of_target

def algorithm_select(y_train):
	output = type_of_target(y_train)
	if output == 'unknown':
		return 0
	if output == 'continuous':
		return 1
	else:
		return 2
