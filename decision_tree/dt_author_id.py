#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
print("the number of features:", len(features_train[0]))
from sklearn import tree
CLF = tree.DecisionTreeClassifier(min_samples_split=40)
T0 = time()
CLF = CLF.fit(features_train, labels_train)
print("decision tree training time:", round(time()-T0, 3), "s")
T1 = time()
PRED = CLF.predict(features_test)
print("decision tree predition time:", round(time()-T1, 3), "s")
ACC = CLF.score(features_test, labels_test)
print(ACC)

#########################################################


