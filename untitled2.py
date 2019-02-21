# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:52:21 2018

@author: sharm
"""

# class
def main():
    a=10
    print(a)

main()
# input fuction takes input from console
input("Enter your Age")

myAge=input("enter your age")
type(myAge)
myAge=int(input("Enter your age"))
type(myAge)
print(myAge)



# concattnation of strings
"Hello" + "World"

# if data types are different then convert it in string and the concatinate

"Hello"+ str(5)

# this does not support - 

"hello"*5


# use triple quotes for preformated statements

print("""First
second
third""")

print("\nHi\nAnuja")

print("\"anuja\"")
print("\\anuja\\")

#unicode characters

print(u'\u0061')

str1="hello"
str2="anuja"

print(str1,str2)
print(str1+str2)

# importing libraries or BATTERIES
import math
dir(math)
help(math.sqrt)

math.sqrt(16)

math.log(16,2)

# making alias of any library

import math as mt
mt.sqrt(64)

from math import sqrt as sq
sq(16)
#  generate random number
import random 
random.randint(0,10)

import os
os.system("cls")

# string slicing

str3= "hello Anuja"

str3[0]
str3[-1] # reverse indexing
str3[6:10]
str3[:10]
str3[0:]
str3[-6:]

str3[:]
str3[::1]
str3[::2]
str3[::-1]

# strings are immutable

# global function -len

len(str3)

# del can free memory : del(variable)



str3.lower()
str3

dir(str)

str3.replace('l','\n')

str3.strip()
str3.find('y')

str3.index('A')

c=str3.split()
type(c)

# for formatting a string :placeholder {} and dot format

name = "anuja"
age = 30
print ("Hello {} you are {} years old".format(name,age))

