# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:38:44 2019

@author: sharm
"""

import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset= pd.read_csv('Income_Data.csv')
features= dataset.iloc[:,:-1].values
labels= dataset.iloc[:,-1].values

#splitting
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test= train_test_split(features, labels, test_size=0.2, random_state=0)

# fitting simple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(features_train, labels_train)

#prdicting
labels_pred= regressor.predict(features_test)

#model score
Score=regressor.score(features_test, labels_test)

#visualization
plt.scatter(features_train, labels_train, color='red')

plt.plot(features_train, regressor.predict(features_train),color='blue')
plt.title("Income vs Experience")
plt.xlabel("ML-Experience")
plt.ylabel("Income")

plt.show()

#Visualize test result
plt.scatter(features_test, labels_test,color="red")
plt.plot(features_train, regressor.predict(features_train),color='blue')
plt.title("Income vs Experience")
plt.xlabel("ML-Experience")
plt.ylabel("Income")
plt.show()