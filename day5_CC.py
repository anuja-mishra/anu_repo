# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:21:55 2018

@author: sharm
"""

"""with open("c:/Users/sharm/Downloads/test/zoo.csv",'r') as file:
    contents=file.readlines()
    print(contents)"""
   
''''import csv
    
with open("c:/Users/sharm/Downloads/test/zoo.csv",'r') as file:
    file_reader=csv.DictReader(file,delimiter=",")
    for row in file_reader:
        print(row[])'''
    
import csv
    
with open("c:/Users/sharm/Downloads/test/zoo.csv",'r') as file:
    file_reader=file.readlines()
    for rows in file_reader:
        print(rows)
    
import csv
with open("c:/Users/sharm/Downloads/test/zoo.csv",'r') as file:
      file_reader= csv.DictReader(file,delimiter=',')
      for rows in file_reader:
          if(rows['animal']=="elephant"):
              print(rows)
          elif(rows['animal']=="lion"):
              print(rows)
         
        
import csv
sum=0
with open("c:/Users/sharm/Downloads/test/zoo.csv",'r') as file:
      file_reader= csv.DictReader(file,delimiter=',')
      for rows in file_reader:
          if(rows['animal']=="elephant"):
              sum+=int(rows['water_need'])
              #print(sum)
print("total water need of elephants is {}".format(sum))


    
import csv
sum=0
with open("c:/Users/sharm/Downloads/test/zoo.csv",'r') as file:
      file_reader= csv.DictReader(file,delimiter=',')
      for rows in file_reader:
          #if(rows['animal']=="elephant"):
           sum+=int(rows['water_need'])
           #print(sum)
print("total water need of all animals is {}".format(sum))

              
