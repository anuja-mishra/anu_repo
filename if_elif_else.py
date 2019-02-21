# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 21:09:06 2019

@author: sharm
"""

""" selection/conditionla branching statements :
    1. if statement
    2. If-else statement
    3. Nested If
    4. If-elif-else statement"""
    
# ..............................................1: if statement
#1.1 program to increment a number if positive

x=10
if(x>0):
    x=x+1
print(x)

#1.2. if a person is eligible to vote
age=int(input("enter the age:"))
if(age>=18):
    print("eligible to vote")
    
#1.3 write a program to determine the character entered by the user
char= input("press a key:")
if(char.isalpha()):
    print("It is an alphabet")
if(char.isdigit()):
    print("It is digit")
if(char.isspace()):
    print("you have entered white space")
    

#................................................2. If-Else
# 2.1. If a person is eligible or not and how many years are left to be eligible
age=int(input("enter your age"))

if(age>=18):
    print("you are eligible to vote")
else:
    yrs=18-age
    print("you have to wait {} format years".format(yrs))
    

#2.2 find larger of two numbers

a= int(input("enter value of a :"))
b= int(input("enter value of b:"))

if(a>b):
    print("a: {} is greater than b: {}".format(a,b))
else:
    print("b: {} is larger than a: {}".format(b,a))
    
#2.3. Whether a given number is even or odd

num= int(input("enter a number"))

if(num%2==0):
    print("It is even")
else:
    print("It is odd")
    
#2.4. Convert a caracter in lower case or upper case

ch=input("enter any alphabet")
if(ch>='A' and ch<='Z'):
    print(ch.lower())
else:
    print(ch.upper())
    

    
#.................................................3. Nested If
#3.1  prompt the user to enter a number and then print its interval

num=int(input("enter a number"))
if(num>=0 and num<10):
    print("range is 0-10")
if(num>=10 and num<20):
    print("range is 10-20")
if(num>=20 and num<30):
    print("range is 20-30")
    
#................................if-elif-else

# 4.1to find whether a number is negative, positive or zero

num=int(input("enter a number"))

if(num==0):
    print("value is equal to zero")
elif(num>0):
    print("number is positive")
else:
    print("number is negative")


# in python we use AND/OR operators to form compund relation expression. 60<=marks<=75 is invalid
# Python uses AND, NOT, OR keywords. It does not allow &&,||, ! boolean logic 
 
 #4.2. find greatest of three number
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))

if(num1>num2):
    if(num1>num3):
        print(num1,"is greater than", num2,"and", num3)
    else:
        print(num3,"is greater than", num1,"and",num2)
elif(num2>num3):
    print(num2,"is greater than",num1,"and",num3)
else:
    print("The three numbers are equal")
    
#4.3. enter number from 1-7 and then print corresponding day of the week

num=int(input("enter a number from 1-7: "))
if(num==1): print("Monday")
elif(num==2): print("Tuesday")
elif(num==3): print("Wednesday")
elif(num==4): print("Thursday")
elif(num==5): print("Friday")
elif(num==6): print("Saturday")
elif(num==7): print("sunday")
else: print("Invalid number entered")
    
#4.4 calculate tax:
""" if income is less than 1,50,000 then no tax
if taxable income is 150001- 3,00,000 then charge 10% tax
if taxable income is 3,00,001-5,00,000 then charge 20% tax
if taxable income is above 5,00,0001 then charge 30% tax
taxable income- income-150000"""



"""4.5. enter marks of student in four subjects. Then calculate the total and aggregate and display the 
grade obtained by the student. If student scores an aggregate greater than 75%, then grade is distinction
. If aggregate is between 60 and 75 then grade is first division. If aggregate is between 50 and 60 then
grade is second division. If aggregate is between 40 and 50 then grade is third division. else fail"""