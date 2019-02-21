# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:21:47 2018

@author: sharm
"""
help(range)
str1=input("enter a number")

number= int(str1)

for r in range(1,number+1):
    for c in range (r):
        print("*",end="")
    print(end='\n')   

for r in range(1,number):
    count=number-r
    for c in range(count):
        print("*",end="")
    print(end='\n')