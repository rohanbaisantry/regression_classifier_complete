
# this program is choose what machine learning algorithm to use.
# note : it is only for supervised learning.
# classification v/s. regression

"""
Idea : 
run though the last column of the data ( the output ) and decide whether they are class labels or if they are continuous values for a regrssion.
return 1 for classification problem and 2 for regression problem.
"""
def algorithmcheck(y_train):
    count = {}
    output = set()
    for x in y_train:
        output.add(x)
    if len(y_train)==len(output):
    	return 2
    for x in output:
	    count[x]=0;
    for i in len(y_train):
	    if y_train[i].isalpha():
		    return 1
	    else:
		    count[y_train[i]]+=1
    if len()

