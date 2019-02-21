# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:42:03 2019

@author: sharm
"""

import numpy as np

str1= "6 9 2 3 5 1 5 4 7"
list1=str1.split(" ")
print(list1)

result=np.asarray((list1))
type(result)
print(result)

print(np.reshape(result.astype(int),(3,3)))