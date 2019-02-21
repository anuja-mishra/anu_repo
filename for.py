# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:22:20 2019

@author: sharm
"""

#1 calculate average of frist n natural numbers
n= int(input("enter the value of n:"))
avg=0.0
s=0
for i in range(1,n+1):
    s=s+i
avg=s/i
print("the sum of first ",n,"natural number is",s)
print("The average of first",n,"natural number is",avg)

#2 print multiplication table of n 

n=int(input("enter any number"))
print("Multiplication table of",n)
print("**********************************************")

for i in range (1,11):
    print(n,"X",i,"=", n*i)
    
    
#3 calculate factorial of a number
num=int(input("enter a number:"))
if(num==0):
    fact=1
    
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num, "is",fact)

#4 if a number is prime or composite

number=int(input("Enter a number"))
iscomposite=0
for i in range(2,number):
    if(number%i==0):
        iscomposite=1
        break
if(iscomposite==1):
    print("number is composite")
else:
    print("number is prime")
    
#5 (for students) read number till -1 is encountered. Count the number of prime numbers and composite numbers entered by a user.

#6 sum of series.....1+1/2+.....+1/n
n= int(input("enter a number"))
s=0
for i in range (1, n+1):
    a=1/i
    s=s+a
print("the sum 1,1/2...1/5 is",s)

#7 (for students) sum of series...1/(1 pow 2)+1/2(2 POW 2)+....1/(N POW 2)
#8  1/2+ 2/3 + .....+ N/(N+1)
#9 1/1+ 2pow2/2 + 3pow3/3+...+npown/n

#10 pattern priting

#10.1 
for i in range(1,6):
    print("PASS",i,"- ",end=' ')
    for j in range (1,6):
        print(j, end=' ')
    print()
    
#10.2
format('Hello','<30')
format('Hello','>30')
format('Hello', '^30')

print('Hello', format('','+<10'),'world')


#10.3
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end=' ')
        
#10.4
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i,end=' ')
        
#10.5
count=0
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count, end=" ")
        count= count+1

#10.6
for i in range(1,6):
    print()
    for s in range (5,i,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
            print(j,end=' ')

#10.7
for i in range(1,6):
    print()
    for s in range (5,i,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(i-1,0,-1):
        print(k,end=" ")
            
    
