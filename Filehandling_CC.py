# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 22:58:08 2018

@author: sharm
"""
help(str.replace)
#code challenge 1
import csv
list1=list()
from collections import Counter
with open("C:/Users/sharm/Downloads/test/romeo.txt","rt") as file:
    file1=file.read().splitlines()
    for line in file1:
        list1+=line.split(' ')
print(list1)
 

       
freq=Counter(list1)
print(freq)

help(hashlib)
#code challenge 2
import hashlib
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
with open("C:/Users/sharm/Downloads/test/romeo.txt","rt") as file:
    file1=file.read()
    print(file1)
    m=hashlib.sha1(file1.encode())
   
    print("ouput:",m.digest())
    

#code challenge 3    
from PIL import Image
img=Image.open("sample1.png")
#info=img.info
#print(info)
size= img.size
print(size)


#code challenge 4-Intersection
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]

a= set(list1)
#print(a)

b=set(list2)
#print(type(b))
#print(a&b)
a.intersection(b)


#code challenge 5-remove duplicates
list1=[12,24,35,24,88,120,155,88,120,155]
resu=list()

for x in list1:
    if x in resu:
        pass
    else:
        resu.append(x)

print(resu)        
print(resu[::-1])