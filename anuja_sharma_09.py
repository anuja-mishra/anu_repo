# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:16:22 2018

@author: sharm
"""

str1= input("enter values")
#for x in str1[1:-1]
list1=list(str1.split(','))
print(list1)

new_list= list1[1:-1]
print(new_list)
sum=0
count=0
for x in new_list:
    sum= sum+int(x)
    count=count+1

print(sum/count)