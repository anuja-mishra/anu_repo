# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:30:55 2018

@author: sharm
"""

state_name=['Albama','California','Oklahoma','Florida']
Vowels=['A','a','E','e','I','i','O','o','U','u']
for x in state_name:
    for y in x:
        if y in Vowels:
            x= x.replace(y,' ')
    print(x)   

help(list.range)
#str1=input("enter items you want to order")
#cart=list()
#print("To quit type DONE")
print("hello")
list2=[1,2,3,4,5,6,7,8,9,10]
print(len(list2))
help(list)

def ADD(crt):
    #crt=list()
    flag=1
    while(flag):
        item=input("Enter a new item\n")
        #ind=input("Enter the index")
        if(item!="DONE"):
            crt.append(item)
        else:
            flag=0
      
def SHOW(crt):
    list1=list(crt)
    len(list1)
    if(len(list1)==0):
        print("cart is empty")
    else:
        for x in range(0,len(list1)):
            print(x,list1[x])
    
def HEL():
    print("to add type add, to quit type DONE, to check list type SHOW and for assistance type HEL")
    
def REMOVE(crt):
    #list2=crt
    ind=input("enter the index number of item which u want to remove")
    del [int(ind)]
    print(list2)
    
def main():
    print("to add type Add, to quit type DONE, to check list type SHOW,for assistance type HELP,\n")
    crt=list()
    fl=1
    while(fl):
        opt=input("Enter  your option:")
    
        if(opt=="Add"):
            ADD(crt)
        elif(opt=="SHOW"):
            SHOW(crt)
        elif(opt=="HELP"):
            HEL()
        elif(opt=="REMOVE"):
            REMOVE(crt)
        else:
            fl=0
              
main()