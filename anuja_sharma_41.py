# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:50:02 2019

@author: sharm
"""

import pandas as pd
df=pd.read_csv("Automobile.csv")
df['price'].head(20)
#df["price"]

df[df.isnull().any(axis=1)]
df['price']=df['price'].fillna(df['price'].mean())
df['price'].head(20)


import numpy as np
#np_aut=np.asarray(df["price"]) way 1 or way 2 below

np_aut=df["price"].values

print(type(np_aut))

np.max(np_aut)
np.min(np_aut)
np.average(np_aut)
np.std(np_aut)