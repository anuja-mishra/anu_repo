# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:25:19 2019

@author: sharm
"""

import matplotlib.pyplot as plt
import pandas as pd


#importing dataset
dataset=pd.read_csv('Data.csv')
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,3].values

#spliting into test and training set
from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)


#graph
plt.scatter(features_train,labels_train)
plt.show()