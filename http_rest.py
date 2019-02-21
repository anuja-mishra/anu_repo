# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:34:57 2018

@author: sharm
"""

import requests
str1=input("enter ur city  name")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+str1
url3="&appid=5bc43d71be2fee03b628f4f2831afafe"

url=url1+url2+url3
res=requests.get(url)
type(res)
# Using urllib2 library
res.content

print(res.text)

print("status code :", str(res.status_code))
print("headers: ", str(res.headers))
for key, value in res.headers.items():
    print(key,':', value)
    
print('content type:', res.headers['Content-Type'])

jsondata=res.json()

print(jsondata)

print (len(jsondata.items()))


jsondata['main']['temp']
print("latitude: ", jsondata['coord']['lat'])
print("longitude: ", jsondata['coord']['lon'])
print("weather: ", jsondata['weather'])
print("wind speed: ", jsondata['wind']['speed'])
print("sunrise: ", jsondata['sys']['sunrise'])
print("sunset: ", jsondata['sys']['sunset'])

# currency convertor

url="https://free.currencyconverterapi.com/api/v6/convert?q=USD_INR,INR_USD&compact=ultra&apiKey=ede7915e7a2030540afb"
response= requests.get(url)
print(response.text)

#post method

urll="http://httpbin.org/#/HTTP_Methods/post_post"
data ={"firstname":"Chris","language":"English"}

response= requests.post(url,data)
response.text



import json

conn = 'http://www.httpbin.org/post'

headers = {'Content-type': 'application/json'}

foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)
requests.post(conn, json_data, headers)

#response = json_data.getresponse()
#print(response.read().decode())
