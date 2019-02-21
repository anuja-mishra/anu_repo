# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:18:43 2018

@author: sharm
"""



def Add(list1):
    add=0
    for x in list1:
        add+=int(x)
    return add      

    

def Mul(list1):
    mul=1
    for x in list1:
        mul*=int(x)
    return mul    
    
   
def Large(list1):
    large=int(list1[0])
    for x in list1:
        if(large<int(x)):
            large=int(x)
    return large
      
def Sorting(list1):
    
    list1.sort()
    print(list1)

def remove_dupli(list1):
    #set1=set()
    print(list(set(list1)))
    

def main():
    list1 =list()
    str1=input("Enter values as list")
    list1=list(str1.split(','))
    add=Add(list1)
    print("Sum : {}".format(add))
    mul=Mul(list1)
    print("Mul : {}".format(mul))
    large=Large(list1)
    print("Largest : {}".format(large))
    Sorting(list1)
    remove_dupli(list1)
    
    
main()    
