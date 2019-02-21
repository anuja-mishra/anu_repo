# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:07:13 2018

@author: sharm
"""
help(str)
#help(random)
words=["banana","apple","guava","grapes","pomegranate","lichi"]
#print(words)
#words[4]="abc"
import random

secret=random.choice(words)
#print(secret)
l=len(secret)
print(l)
chance=3
letters=list()

while(chance):
    
    guess=input("Guess an alphabet")
    if(l>1):
        if guess in secret:
            print("found")
            l=l-1
            #print(l)
            letters.append(guess)
            
        else:
            chance= chance-1
            print("You have {} chances".format(chance))
            
    else:
            print("your guesses are")
            print(letters)
            word=input("Now reaarange")
            if(word==secret):
                print("voila!! U WON")
                break
  
