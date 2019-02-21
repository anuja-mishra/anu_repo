# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:29:47 2019

@author: sharm
"""

import numpy as np
import matplotlib.pyplot as plt

val= np.random.normal(150,20,1000)
plt.hist(val,100)

np.std(val)
np.var(val)