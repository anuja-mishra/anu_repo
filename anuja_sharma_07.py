# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:06:44 2018

@author: sharm
"""
help(str)
help(list.append)
    
str1=input("enter a string")
list1=list(str1)
print(list1)
from collections import Counter

frequency=Counter(list1)
print(frequency)