# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:35:22 2019

@author: sharm
"""
import pandas as pd
df=pd.read_csv("training_titanic.csv")
df_surv=df[df["Survived"]==1]
df_surv.count()
# calculate number of passengers survived and died using value_counts()
df['Survived'].value_counts()

df['Survived'].value_counts(normalize=True)

df_f=df[df['Sex']=='female']['Survived'].value_counts()
#or
df_f=df[df['Sex']=='female']
df_f['Survived'].value_counts()
df_f['Survived'].value_counts(normalize=True)
print(df_f)

df_m=df[df['Sex']=='male']
df_m['Survived'].value_counts()
df_m['Survived'].value_counts(normalize=True)

