# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:23:58 2019

@author: sharm
"""

import matplotlib.pyplot as plt
import numpy as np
incomes = np.random.normal(100.0, 20.0, 10000)
print(incomes)
plt.hist(incomes,50)
np.mean(incomes)
np.median(incomes)
incomes=np.append(incomes,[100000000])
plt.hist(incomes,50)
