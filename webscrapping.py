# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:49:09 2018

@author: sharm
"""

from bs4 import BeautifulSoup
import requests

with open("C:/Users/sharm/Downloads/test/simple.html") as html_file:
    soup=BeautifulSoup(html_file,"lxml")
    
print(soup)

#indent data
print(soup.prettify())

#read data
print(soup.title)
print(soup.title.text)

print(soup.div)
print(soup.div.h1.text)

first_div= soup.find("div")
print(first_div)

all_div=soup.find("div","footer")
print(all_div)
print(all_div.h2.text)


for article in soup.find_all("div"):
   # print(article)
    print(article.p.text)
    
# reading from web page

source=requests.get("http://httpbin.org/html").text
soup=BeautifulSoup(source,"lxml")
print(soup)

print(soup.prettify())
print(soup.head)
print(soup.body)
print(soup.body.div)
print(soup.body.div.p)
print(soup.body.div.p.text)



source=requests.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India").text
soup=BeautifulSoup(source,"lxml")

print(soup.prettify())

tar_table=soup.find("table","wikitable")
print(tar_table)
print(tar_table.prettify())

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]


for rows in tar_table.findAll("tr"):
    cells=rows.findAll("td")
    states=rows.findAll("th")
    if(len(cells)==5):
        A.append(str(cells[0].find(text=True)))
        B.append(str(states[1].find(text=True)))
    
print(A)
print(B)
print(len(cells))
print(len(states))

import pandas as pd
df=pd.DataFrame()
df['capital']=A
df['state']=B

df.to_csv("wikidata.csv")
print(df)


source=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
soup=BeautifulSoup(source,"lxml")

print(soup.prettify())

tab_data=soup.find("table","table")
print(tab_data.prettify())

team=[]
matches=[]
ranking=[]
for rows in tab_data.findAll("tr"):
    cells=rows.findAll("td")
    
    if(len(cells)==5):
        team.append(str(cells[1].find(text=True)))
        matches.append(str(cells[2].find(text=True)))
        ranking.append(str(cells[4].find(text=True)))
    
print(len(cells))
print(matches)

import pandas as pd
df=pd.DataFrame()
df['Team']=team
df['Matches']=matches
df['Ranking']=ranking

df.to_csv("ICC_Rank.csv")
print(df)

