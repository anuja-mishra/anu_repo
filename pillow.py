# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:05:54 2018

@author: sharm
"""

# for-else and while -else

import  logging
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='c:/Users/sharm/Downloads/test/game.log', level=logging.DEBUG)



logging.debug("this is a debug message")
logging.info("This is a informational message")
logging.warning("this is warning message")
logging.error("This is a error message")
logging.critical("This is a critical error")

#Dictionary
dict1= dict()
print(dict1)
dict2={}
dict3= dict({})
print(dict2,dict3)


dict1={'fname':'Anuja','lname':'Sharma', 'profession':'Teaching'}
print(dict1)

#Add or Update
dict1['lname']='Mishra' #update a value

dict1['city']='Jaipur' #add a key

dict1.update({'city':'Gurgaon', 'lname':'sharma mishra'})

#printing values

print(dict1['lname'])

print(dict1.get('fname'))

print(dict1.get('sal','NOT FOUND'))
dict1['city']='jaipur'
my_string=print("HI my name is {fname} and I live in {city}".format(**dict1))
dict1['sal']='none'
print(dict1)

# remove  a dcitionary
del dict1['sal']

print(dict1)
dict1.pop('sal')
print(dict1)


# To list all keys
print(dict1.keys()) # returns a list of keys

# to list all values
dict1.values()

for keys in dict1.keys():
    print(keys)
    
for values in dict1.values():
    print(values)
    
# toprint all values and keys
    
for keys in dict1:
    print(keys,dict1[keys])
    
# looping in dictionary

for key,value in dict1.items():
    print(key,value)

# generate frequency

words= ["One", "Two","One","Three","One"]
freq=dict()

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

for word in freq.keys():
    print(word,":",freq[word])    
    
# alternate way to find frequencey
from collections import Counter
words= ["One", "Two","One","Three","One"]
frequency= Counter(words)
print(frequency)

# study ordered sictionary and named tuple

# set
# It stores unique values
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}



