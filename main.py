
# This is the main program

"""

The first major step to apply is feature selection or feature extraction (dimensionality reduction). This is a pre-processing step that you can apply using certain relevance metrics like correlation, mutual-information as mRmR. Also, there are other methods stimulated by the domain of numerical linear algebra and statistics such as principle component analysis for finding features describing the space based on some assumptions.

Your question is related to a major concern in the field of machine learning known as model selection. The only way to know which degree to use is to experiment with models of different degrees (d=1, d=2, ...) keeping in mind the following:

1- Overfitting: you need to avoid overfitting by making sure that you limit the ranges of the variables (the Ws in your case). This solution is known as regularization. Also, try not to train the classifier for long time like in the case of ANN.

2- Prapring training, validation and testing sets. Training is for training the model, validation is for tuning the parameters and testing is for comparing different models.

3- Proper choice of the performance evaluation metric. If your training data is not well-balanced (i.e. nearly the same number of samples is assigned for each value or class lable of your target variable), then accuracy is not indicative. In this case, you may need to consider sensitivity, specificity or Mathew correlation.

Experiments is the key and indeed you are limited by resources. Nevertheless, proper design of the experiment could serve your purpose

"""

# START

import load
import algorithm_selection
import normality_check
import scaling_standardization
import hypothesis_selection
import feature_selection
import accuracy 
from boruta import BorutaPy
