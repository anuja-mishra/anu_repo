# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:34:53 2019

@author: sharm
"""

'''Program Specification

Import the local file cars.csv and split the data set equally into test set and training set (don't forget to consider dependent and independent variables).

Print it and save all the datasets  into separate '.csv' files.'''

import pandas as pd

df=pd.read_csv('Cars.csv')

features=df.iloc[:,1:]
labels=df.iloc[:,0]

# splitting dataset 

from sklearn.cross_validation import train_test_split

f_train, f_test, l_train, l_test= train_test_split(features, labels, test_size=0.5, random_state=0)

f_train.to_csv('feature_train.csv')     
f_test.to_csv('Feature_test.csv')
l_train.to_csv('Label_train.csv')
l_test.to_csv('Label_test.csv')