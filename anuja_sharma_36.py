# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:02:03 2019

@author: sharm
"""
import pandas as pd

df=pd.read_csv("training_titanic.csv")
#df['child']=0
# method 1
Child=[]

for i in df.Age:
    if(i<18):
        Child.append(1)
    else:
        Child.append(0)
        
Child[0:10]
len(Child)

child_series=pd.Series(Child)
child_series.head(10)
df.insert(12,'child',child_series)

df['child'].value_counts()
df['child'].value_counts(normalize=True)

#Method 2
df=df.fillna(df.mean())
df['child']=df['Age'].apply(lambda x:1 if x<18 else 0)
df['child'].value_counts()