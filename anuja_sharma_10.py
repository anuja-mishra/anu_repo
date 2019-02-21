# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:18:03 2018

@author: sharm
"""
help(list)
str1=input("enter numbers")
list1=list(str1.split(','))
for x in list1:
    if(x=="13"):
        indexer=list1.index("13")
        del list1[indexer]
        del list1[indexer]
print(list1)

for x in list1:
    sum+=int(x)
print(sum)