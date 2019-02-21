# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:07:24 2019

@author: sharm
"""

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Foodtruck.csv')
df_features=df.iloc[:,:-1].values
df_labels=df.iloc[:,-1].values

# training dataset
from sklearn.cross_validation import train_test_split
f_train, f_test,l_train, l_test=train_test_split(df_features, df_labels, test_size=0.2,random_state=0 )

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(f_train,l_train)





#predict
labels_pred=regressor.predict(f_test)

#model score
score=regressor.score(f_test,l_test)

plt.scatter(f_test,l_test, color='red')
plt.plot(f_train,regressor.predict(f_train),color='blue')
plt.xlabel("Population")
plt.ylabel("Profit")
plt.show()


result=regressor.predict(3.073)
print(result)
