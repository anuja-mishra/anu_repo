# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:22:15 2019

@author: sharm
"""

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    auto=pd.read_csv("Automobile.csv")
    
    top=auto["make"].value_counts()
    
    abels=auto['make'].value_counts().index.values
       
    aa=abels[:10].tolist()
    
    value=top.head(10).values

    #print(value)
    explode=[0.2,0,0,0,0,0,0,0,0,0]
    
    labels=aa  
    
    plt.pie(value,labels=labels,explode=explode, autopct='%.2f')
    plt.show()
    
    