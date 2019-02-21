# -*- coding: utf-dir8 -*-
"""
Created on Sat Oct 13 16:58:12 2018

@author: sharm
"""
#comparision operator

#same as used in C

# looping

if(5==6):
    print ('its true')
elif(5==6):
    print('are youu nits')
    
else:
    print('it is false')
    
    

    
x= None

bool(x)
n=0
while(n<10):
    print('n')
    n+=1
    
    
#List
# it can store different types of data type in one list

# create a list and initialize ir : methos 1
empty_list = [1,2,3,'abc',"abc"]

list1= list()
list1= empty_list
len(list1)
print (type(list1))

print(empty_list)

list1.append(4)
print(list1)

list1.insert(0,3)
print(list1)
list1.remove(3)

print(list1)

list1.pop()

del list1[0:2]

print(list1)

print(list1[0:5:2])




list2=[3,2,6 ,5, 9,7,8]
print(list2)

list2.sort()
print(list2)


x=[0,1,2]
y=[3,4,5]
# This appends list y to list x; so at 3rd index complete list is appended

x.append(y)

print(x)
# to print value at index 0 of inner list
print(x[3][0])


# if want to append values of one list to otehr list then use extend or use +

x.extend(y)
print(x)

print(x+y)
# to generate a list

z=list(range(13))
print(type(z))
print(z)

# for loop
for x in list2:
    print(x)

#break, continue and pass



def hello(abc):
    print("hello {} anuja".format(abc))
    print("hello all")
    
    
print(hello("to"))


# simultaneus assignments

a,b=1,"good"

print(a)
print(b)

#packing
c=(3,4)
print (type(c))
print (c)

#unpacking

d,e=c

print(d)
print(e)

names_of_days=('mon','tues','wed','thur','fri','sat','sun')

print(names_of_days)

a,b=b,a

print(a)

print(c+names_of_days)

Q,r=divmod(23,2)

print(Q)
print(r)

# enumerate creates a tuple

for index,item in enumerate(names_of_days):
    print("{}:{}".format(index,item))
    
#or use for step and then in print use .format(step[0],step[1])
    
for step in enumerate(names_of_days):
    print("{}:{}".format(step[0],step[1]))

# or use .format(*step)

for step in enumerate(names_of_days):
    print("{}:{}".format(*step))
    
    
import calendar
yy=int(input("enter your year"))
mm=int(input("enter your month"))
print(calendar.month(yy,mm))  

from datetime import date
d0= date(2018,1,1)
d1= date(2018,1,11)
differ= d1-d0
print(differ)