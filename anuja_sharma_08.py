# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:48:04 2018

@author: sharm
"""

str1=input("enter a string")
letter=0
digit=0
for x in str1:
    if(x.isalpha()):
        letter= letter +1
    elif(x.isdigit()):
        digit= digit+1
print("letter : {} and digit: {}".format(letter, digit))