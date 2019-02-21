# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:23:42 2018

@author: sharm
"""



print(str(23))

print(14%4)

name = input("enter your name")

print(name)

print("""This is a multi line stirng. This code challenge is to 
    test your understanding about strings. You need to print  some part of this string.
    From here print this text without manually counting the indexes.""")
    
    
str1="""This is a multi line stirng. This code challenge is to 
test your understanding about strings. You need to print  some part of this string.
From here print this text without manually counting the indexes."""


a=str1.index('F')
print(str1[a:])



# code 2
str2="Welcome to Pink City Jaipur "

help(str.replace)

str2.replace(" ","*")


#code 3

dir(str)
help(str)

str3="Welcome to Pink City Jaipur "
res="*".join(str3)
print(res)

#code 4

st= input("enter you statement")
print(st)
sp=st.split(" ")

print(" ".join(sp[::-1]))



print((6+12)*3)
resu=sp[::-1]
print(resu)




int(29.69)
print("3" * "hello")

import  math
math.sqrt(16)


a=3
type(x)
print(x)
a+2.0

a=a+1.0

print(a)


print('a\'bc\'d\nof\\nmp')




str1="Forsk Technologies"
str1[-7:]

_2="HarryPotter"
print(_2)

words=str1.split(' ')
print(words)

str4="A sring is a sequence of one or more characters"
str4.split(' ',5)

os="mac"
ver="6S"
mob="iphone"
print("I have an {0} uses {2} and model{1}".format(mob,ver,os))