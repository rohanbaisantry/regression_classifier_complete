
#Program to Load the data

# Headers 
import pandas as pd
import numpy as np

#Loading the dataset as numpy arrays
def load(train_str,test_str):
    training_data = np.array( pd.read_csv( train_str, sep = ",", header = None ))
    testing_data = np.array( pd.read_csv( test_str, sep = ",", header = None ))
    m=len(training_data) # Number of rows of training data
    number_of_features=len(training_data[0])-1
    n=len(testing_data) # number of rows of testing data
    x_train=training_data[:, :-1]
    y_train=[ row[-1] for row in training_data ]
    x_test=testing_data[:,:-1]
    y_test=[ row[-1] for row in testing_data ]
    return [x_train, y_train, x_test, y_test, m, n, number_of_features]
