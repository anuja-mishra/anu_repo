# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:03:59 2018

@author: sharm
"""

#file handling
"""mode of file : READ-r WRITE-w APPEND-a CREATE-x
1. to open a file use open()

"""

file=open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt")

print(file.name)
print(file.mode)
print(file.closed)

file.close()
print(file.closed)

try:    
    file=open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt")

    print(file.name)

except IOError:
    
    print("File not found")
except Exception:
    print("ok ok")
    
finally:
    file.close()

  #read   
with open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt") as file:
    file_contents1=file.read()
    print(file_contents1)
    
    
with open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt") as file:
    file_contents2=file.readline()
    print(file_contents2)
    
with open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt") as file:
    file_contents3=file.readlines()
    print(file_contents3)

with open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt") as file:
    for line in file:
        print(line)
  
with open("c:/Users/sharm/Downloads/test/anuja_sharma_01.py","rt") as file:
    file_contents4=file.read(5)
    print(file_contents4)
    position=file.tell()
    print(position)
    
    file.seek(10)
    
    file_contents4=file.read(50)
    print(file_contents4)
   
# write operation

file=open("c:/Users/sharm/Downloads/test/untitled0.py","wt")
file.write("NOW THIS IS IT")
file.close()

file=open("c:/Users/sharm/Downloads/test/untitled0.py","at")

file.writelines(["second", "Third","Fourth"])
file.close()


# how to read and write non text file
with open("c:/Users/sharm/Pictures/3.jpg","rb") as file:
    with open("c:/Users/sharm/Pictures/copy.jpg","wb") as copy_file:
        for lines in file:
            copy_file.write(lines)
            


import os
os.getcwd()
os.chdir("d:/python class")
os.getcwd()
os.path.exists("abc.zoo")


os.remove("file name")
os.makedirs("myFolder")
os.getcwd()
os.rmdir("myFolder")
os.chdir("c:/Users/sharm/Downloads/test")


    
import csv
with open("C:/Users/sharm/Downloads/test/Salaries.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)
        

with open("C:/Users/sharm/Downloads/test/Salaries.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row[5])
        
# To skip header information
with open("C:/Users/sharm/Downloads/test/Salaries.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
        
# to use as dictionary
with open("C:/Users/sharm/Downloads/test/Salaries.csv") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for row in csv_reader:
        #print(row)
        print(row['salary'])
        
import csv

with open("C:/Users/sharm/Downloads/test/employee.csv",'w') as cf:
    cf_writer=csv.writer(cf, delimiter=",",quotechar='"')
    cf_writer.writerow(['Anuja','CSE','sept'])
    cf_writer.writerow(['Abhishek','MECH','JUNE'])
    cf_writer.writerow(['Amayra','CSE','May'])