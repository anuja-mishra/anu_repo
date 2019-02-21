# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:10:21 2018

@author: sharm
"""
help(str.strip)
help(range)
dict1={}
#dict1=dict(str1[1:len(str1)-1])
list1=['a','b','c']


for x in list1:
    str1=input("enter number:")
    dict1[x]=int(str1)


#print(dict1)
#dict1={"a":2,"b":15,"c":19}
sum=0
for values in dict1.values():
    if values in range(13,20):
        if(values!=15 & values!=16):
            values=0
            
    sum+=values
print(sum)