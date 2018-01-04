#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

# reducing training datasets number to 1% in order to increase the speed
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

# training codes below for svc kernel linear
from sklearn.svm import SVC
import numpy as np
CLF = SVC(kernel='linear')
T0 = time()
CLF.fit(features_train, labels_train)
print("svm linear training time:", round(time()-T0, 3), "s")
T1 = time()
PRED = CLF.predict(features_test)
print("svm linear predition time:", round(time()-T1, 3), "s")
ACC = CLF.score(features_test, labels_test)
print(ACC)

# training codes below for svc kernel rbf
CLF = SVC(kernel='rbf', C=10000)
T0 = time()
CLF.fit(features_train, labels_train)
print("svm rbf training time:", round(time()-T0, 3), "s")
T1 = time()
PRED = CLF.predict(features_test)
print("svm rbf predition time:", round(time()-T1, 3), "s")
print("preditions[10]:", PRED[10], "preditions[26]:", PRED[26], "preditions[50]:", PRED[50])
print("total preditions:", np.sum(PRED))
ACC = CLF.score(features_test, labels_test)
print(ACC)

#########################################################


