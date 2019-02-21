# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:09:03 2019

@author: sharm
"""

# use of while loop

#1 print first 10 number
i=0
while(i<=10):
    print(i,end=" ") # can use end= '\t'
    i=i+1 
    
#2 calculate sum and average of first 10 numbers

i=0
s=0
while(i<=10):
    s=s+i
    i=i+1
avg= s/10
print("sum of first 10 numbers is: ",s)
print("average of first 10 numbers is: ",avg)

# 3 print 20 horizontal *  


# 4 calculate the sum of numbers from m to n
m = int(input("enter the value of m: "))
n = int(input("enter the value of n: "))
s=0
while(m<=n):
    s=s+m
    m=m+1
print("sum",s)

# 5 count number of negatives, positives and zeros entered by user until -1 is encountered
negatives=positives=zeros=0
print("enter -1 to exit...")
while(1):
    num=int(input("enter a number: "))
    if(num == -1):
        break
    elif(num==0):
        zeros= zeros+1
    elif(num>0):
        positives= positives+1
    else:
        negatives=negatives+1
        
print("count of zeros enteres:", zeros)
print("count of positives enteres", positives)
print("count of negatives entered: ", negatives)

#6 find whether a number is armstrong number. example 371

n= int(input("enter a number"))
s=0
num=n
while(n>0):
    r=n%10
    s=s+(r**3)
    n=n//10
    print(s,n)

if(s==num):
    print("The number is armstrong",s)
else:
    print("number is not a armstrong",s)

    
#7 ask user for a number and then print countdown from that number to zero

n=int(input("enter any number"))

while(n>0):
    print(n, end=' ')
    n= n-1
