# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:56:30 2019

@author: sharm
"""

#list concatenation
[1,2,3,4]+[2,7,8,9]

# in
list1=['a','e','i','o','u']
if 'a' in list1:
    print("exists")
    
#not in
list1=['a','e','i','o','u']
if 't' in list1:
    print("exists")
else:
    print("does not exist")
    
# max
list2=[0,21,43,56,13,12,16,17,81,99]

print(max(list2))
# min 
print(min(list2))
# sum
result=sum(list2)
print(result)

#all
list3=[-1,2,3,]
print(all(list3))
#any
list4=[]
print(any(list4))

# list
list4=list("hello")
print(list4)

#sorted
print(sorted(list2))

# list indexin and slicing
list_A= ["Hello","Good","Morning"]
print(list_A[2])
print(list_A[-3])

print(list_A[1:])

#list Methods.....append
list2=[10,12,43,56,13,12,16,17,81,99]

print(list2.append(500))
print(list2)

# count
print(list2.count(12))

#index
print(list2.index(12))

#insert
print(list2.insert(5,250))

print(list2)

#pop
print(list2.pop(4))
print(list2)

#remove
print(list2.remove(250))
print(list2)

#reverse
print(list2.reverse())
print(list2)

#sort()
print(list2.sort())
print(list2)
#extend
list1.extend(list2)
print(list1)

#list within list 
list1=[1,2,3]
list2=['a','b','c']
list1.append(list2)
print(list1)
print(list1[3][1])
#delete in list
list2=[10,12,43,56,13,12,16,17,81,99]
del list2[3]
print(list2)
#way 2 to delete
list2[2:5]=[]
print(list2)