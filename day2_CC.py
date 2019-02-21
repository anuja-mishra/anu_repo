# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:30:55 2018

@author: sharm
"""

state_name=['Albama','California','Oklahoma','Florida']
Vowels=['A','a','E','e','I','i','O','o','U','u']
word=[]
for x in state_name:
    str1=""
    for y in x:
        if y in Vowels:
            pass
           # x= x.replace(y,' ')
           #x=x.
        else:
            str1=str1+y
    #print(x)   
    word.append(str1)
print(word)

    
list2=['a','b','c']
str1=""
for i in list2:
    str1=str1+i
print(str1)
    
    
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
        ind=input("do you wnat to enter on particular index: Yes or No")
        item=input("Enter a new item\n")
        if(ind!="Yes"):
            
            if(item!="DONE"):
                crt.append(item)
            else:
                flag=0
        else:
            index=input("enter index value")
            index_no=int(index)
            crt.insert(index_no,item)


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
    del crt[int(ind)]
    print(crt)
    
def main():
    print("to add type ADD, to quit type DONE, to check list type SHOW,for assistance type HELP,\n")
    crt=list()
    fl=1
    while(fl):
        opt=input("Enter  your option:")
    
        if(opt=="ADD"):
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