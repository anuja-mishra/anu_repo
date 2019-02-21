# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:02:52 2019

@author: sharm
"""

from bs4 import BeautifulSoup
import requests

source=requests.get("https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area").text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())

tar_table=soup.find("table","wikitable")
#print(tar_table.prettify())

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]


for rows in tar_table.findAll("tr"):
    cells=rows.findAll("td")
    if(len(cells)==7):
        
        A.append(str(cells[1].find(text=True)))
        B.append(str(cells[4].find(text=True)))       
    
print(A)
print(B)

import matplotlib.pyplot as plt

values= B[:6]
labels=A[:6]
explode=[0.2,0,0,0,0,0]
plt.pie(values, labels=labels,explode=explode,autopct='%.2f')
plt.title("National share ")
plt.show()