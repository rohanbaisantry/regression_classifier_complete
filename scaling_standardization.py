
# program for scaling and standardizing the Data.

from numpy import std
from numpy import mean

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
	    col_values = [row[i] for row in dataset]
	    value_min = min(col_values)
	    value_max = max(col_values)
	    minmax.append([value_min, value_max])
    return minmax

# Rescale dataset columns to the range 0-1
def Scaling_dataset(dataset, minmax):
    for row in dataset:
	    for i in range(len(row)):
		    row[i] = (row[i] - minmax[i][0]) / float(minmax[i][1] - minmax[i][0])

# to calculate variance and mean
def dataset_stdmean(dataset):
    stdmean=list()
    for i in range(len(dataset[0])):
        col_values=[row[i] for row in dataset]
        value_var=var(col_values)
        value_mean=mean(col_values)
        stdmean.append([value_var, value_mean])
    return stdmean

# stadardize the columns 
def standardizing_dataset(dataset, stdmean):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][1]) / float(minmax[i][0])

# Scaling the datasets 
def scaling(x_train,x_test):
    # Scaling the training data
    minmax_train=dataset_minmax(x_train)
    Scaling_dataset(x_train,minmax_train)
    # Scaling the testing data
    minmax_test=dataset_minmax(x_test)
    Scaling_dataset(x_test,minmax_test) 
    return [x_train, y_train, x_test, y_test]

# standardizing the data
def standardizing(x_train,x_test):
    # Standardizing the training data
    stdmean_train=dataset_stdmean(x_train)
    Standardizing_dataset(x_train,stdmean_train)
    # Standardizing the testing data
    stdmean_test=dataset_stdmean(x_test)
    Standardizing_dataset(x_test,stdmean_test) 
    return [x_train, y_train, x_test, y_test]