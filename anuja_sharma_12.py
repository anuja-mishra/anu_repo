# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:10:18 2018

@author: sharm
"""

str1=input("enter number of small bricks, large bricks and target length in sequence")
list1=list()
for x in str1.split(','):
    list1.append(x)
 
print(list1)

small=1*int(list1[0])
large=5*int(list1[1])
total=small+large
print(total)

if(total>=int(list1[2])):
    print("True")
else:
    print("False")
    
    
    
    
            