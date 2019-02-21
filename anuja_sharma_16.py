# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:55:03 2018

@author: sharm
"""

help(str)
str1="This is fun"
list1=['a','A','e','E','i','I','o','O','u','U',' ']

for x in str1:
    if x in list1:
        print(x,end='')
        #x.join(str2)
        pass
    else:
        #print(str1.index(x))
        str2=x + "o" +x
        #print(str2)
        
        print(str2, end='')