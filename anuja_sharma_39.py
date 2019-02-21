# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:36:06 2019

@author: sharmnp.random(40)
"""

import numpy as np

a=np.array(5)
a=np.random.uniform(low=5, high=15, size=(50))

b=np.random.randint(5,15,60)
print(b)
#without nparray
from collections import Counter
freq=Counter(b)
print(freq)

#with nparray
uni,count=np.unique(b,return_counts=True)
print(uni,count)
ind=np.argmax(count)
print(ind)
print(uni[ind])



