
# This is the main program

"""
The first major step to apply is feature selection or feature extraction (dimensionality reduction). This is a pre-processing step that you can apply using certain relevance metrics like correlation, mutual-information as mRmR. Also, there are other methods stimulated by the domain of numerical linear algebra and statistics such as principle component analysis for finding features describing the space based on some assumptions.

Your question is related to a major concern in the field of machine learning known as model selection. The only way to know which degree to use is to experiment with models of different degrees (d=1, d=2, ...) keeping in mind the following:

1- Overfitting: you need to avoid overfitting by making sure that you limit the ranges of the variables (the Ws in your case). This solution is known as regularization. Also, try not to train the classifier for long time like in the case of ANN.

2- Prapring training, validation and testing sets. Training is for training the model, validation is for tuning the parameters and testing is for comparing different models.

3- Proper choice of the performance evaluation metric. If your training data is not well-balanced (i.e. nearly the same number of samples is assigned for each value or class lable of your target variable), then accuracy is not indicative. In this case, you may need to consider sensitivity, specificity or Mathew correlation.
"""

"""

Algorithms used for Regression : Single VariableLinear Regression, Multivariate linear regression, Polynomial Regression, Lasso Regression, Support Vector Machine and Decision Trees Regressor.
Algorithms used for Classification : Logisitic Regression, Support Vector Machine, Decision Trees and Random Foressts.

Evaluation Metrics for Regression : Root Mean Square Error, Mean Absolute Error and R2 Score ( R squared Score).
Evaluation Mterics for Classification : Accuracy Percentage and The Confusion Matrix. 

Conditions for the program to work :
1) The Data set should be in .csv format
2) The output should be only of a single dimension.

"""

# START

import load
#import normality_check
import scaling_standardization
import hypothesis_selection
#import feature_selection
import accuracy 
import error
import algorithm_selection

# Step 1 : Loading
import load

print(" \n\n START \n\n ")
# ask for the names of the testing and training data ( accepts only csv files )
train_str=input("\n\n  Enter the name of the Training file : ")
test_str=input("\n\n  Enter the name of the Testing file : ")
# Loading the files and getting the reqired data from it using the load function in the load.py module
x_train, y_train, x_test, y_test, m, n, number_of_features = load.loading(train_str, test_str)

# Step 2 : Algorithm Selection : Classification or Regression
import algorithm_selection

classification_regression = algorithm_selection.algorithm_select(y_train)
if classification_regression == 1:
	print("\n\n Regression Problem")
elif classification_regression == 2:
	print("\n\n Classification Problem")
elif classification_regression == 0:
	# ask the user if it is a classification or regression problem
	while( not( (classification_regression == 1) or (classification_regression == 2) ) ):
		classification_regression = int(input(" \n\n Unable to automatically detect.\n\n Problem type selection : \n  -> Press '1' if it is a Regression Problem\n  -> Press '2' if it is a Classification Problem \n "))
		if classification_regression == 1:
			print("\n\n Regression Problem")
		elif classification_regression == 2:
			print("\n\n Classification Problem")
		else:
			print("\n wrong input! enter again!")

# Step 3 : Scaling or Standardization or nothing
import scaling_standardization
scaling_or_standardizing = 1 # if scaling_or_standardizing = 0: nothing is done; = 1: scaling is done; = 2: standardization is done.

# checks for choosing between sclaing and standardization.

if scaling_or_standardizing == 2:
	# Standardizing the data
	x_train, x_test = scaling_standardization.standardizing(x_train, x_test)
elif scaling_or_standardizing == 1:
	# Scaling the data
	x_train, x_test = scaling_standardization.scaling(x_train, x_test)

# if it's a classification problem, get the number of output classes
number_of_classes = 0 # number_of_classes =0: Regression Problem; =n (some number): classification problem with n output classes 
if classification_regression==2:
	classes = set()
	for x in y_train:
		classes.add(x)
	number_of_classes = len(classes)
	print("\n Number of output classes = "+ str(number_of_classes))

# step 4 : Check for normality
from normality_check import normality_checking

normality = normality_checking(x_train)
if  number_of_features == len(normality):
	print ("equal")


"""
#  running the algorithms for regression
import regression
if classification_regression == 1:

# traininng and testing -> output is a list of array of the different errors
y_pred_regression = list()

y_pred_regression.append(regression.linear_regression(x_train, y_train, number_of_features, x_test, y_test))
y_pred_regression.append(regression.multiple_regression(x_train, y_train, number_of_features, x_test, y_test))
y_pred_regression.append(regression.lasso_regression(x_train, y_train, number_of_features, x_test, y_test))
y_pred_regression.append(regression.svm_regression(x_train, y_train, number_of_features, x_test, y_test))
y_pred_regression.append(regression.polynomial_regression(x_train, y_train, number_of_features, x_test, y_test))


# printing the outputs


# running the algorithms for classification
if classification_regression == 2:

# training and testing -> output is a list of array of the different accuracies
y_pred_classification = list()

y_pred_classification.append(logistic_regression(x_train, y_train, number_of_features, number_of_classes, number_of_features, x_test, y_test))
y_pred_classification.append(svm_classification(x_train, y_train, number_of_features, number_of_classes, number_of_features, x_test, y_test))
y_pred_classification.append(decision_trees(x_train, y_train, number_of_features, number_of_classes, number_of_features, x_test, y_test))
y_pred_classification.append(random_forest(x_train, y_train, number_of_features, number_of_classes, number_of_features, x_test, y_test))

# printing the outputs


"""

# END OF PROGRAM
