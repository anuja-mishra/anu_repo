# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:43:24 2018

@author: sharm
"""

str1=input("enter numbers seperated by commas:")

list1=list(str1.split(','))
print(list1)
type(list1)


tuple1=tuple(str1.split(','))
print(tuple1)
type(tuple1)