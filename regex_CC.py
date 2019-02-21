# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:11:13 2019

@author: sharm
"""
import re

N= input("enter a a floating point number")


regex=re.compile(r'^[+-]?\d*\.[0-9]+')
response=regex.match(N)
if response:
    print(response.group())
else:
    print("NOT FLOAT")
    
    
    
import re

str1=input("Enter a string")
#regex=re.compile(r'^[\w\d-]+@[\w\d]+\.[\w]{2,4}',str1)
response=re.findall(r'^[\w\d-]+@[\w\d]+\.[\w]{2,4}',str1)
print(response)
    

str2=input("enter your card number")
response=re.findall(r'^[4,5,6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',str2)
print(response)


str1="Anuja"
str1[1:-1]
    
    