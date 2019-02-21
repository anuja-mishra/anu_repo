# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:18:56 2019

@author: sharm
"""

import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv("Bahubali2_vs_Dangal.csv")
features=df.iloc[:,:-2]
bahu_label=df.iloc[:,-2]
Dangal_label=df.iloc[:,-1]
# split
from sklearn.cross_validation import train_test_split
f_train,f_test,bahu_l_train,bahu_l_test= train_test_split(features,bahu_label, test_size=0.2,random_state=0)

f_train,f_test,dangal_l_train,dangal_l_test=train_test_split(features,Dangal_label,test_size=0.2,random_state=0)

# regressor
from sklearn.linear_model import LinearRegression
regressor_bahu=LinearRegression()
regressor_Dangal=LinearRegression()

regressor_bahu.fit(f_train,bahu_l_train)
regressor_Dangal.fit(f_train,dangal_l_train)

#labels_pred=regressor_bahu.predict(f_test)


#visualize
#plt.scatter(f_test,bahu_l_test,color='red')
plt.scatter(10,regressor_bahu.predict(10),color='red',s=200)
plt.plot(f_train, regressor_bahu.predict(f_train),color='red')

#plt.scatter(f_test,dangal_l_test,color='green')
plt.scatter(10,regressor_Dangal.predict(10),color='green',s=200)
plt.plot(f_train, regressor_Dangal.predict(f_train), color='green')

plt.show()


print(regressor_bahu.predict(10))
print(regressor_Dangal.predict(10))