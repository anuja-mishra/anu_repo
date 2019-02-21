# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:20:39 2018

@author: sharm
"""


import json


json_string="""{
	"resercher": {
		"name": "Fordperfect",
		"species": "Betelgusian",
		"relative": [{
			"name": "Zaphod Beeblebrox",
			"species": "Betelgusian"
		}]
	}

}"""
print(type(json_string))

# convert json data type to python data type
my_data=json.loads(json_string)
print(type(my_data))

print(my_data)

print(my_data['resercher'])
print(my_data['resercher']['relative'][0])
print(my_data['resercher']['relative'][0]['name'])

#converts Python data types to JSON Data types
new_json=json.dumps(my_data)

print(type(new_json))
print(new_json)

new_json=json.dumps(my_data,indent=2)
print(new_json)

new_json=json.dumps(my_data,indent=2,sort_keys=True)
print(new_json)

#writing json into a file
with open("C:/Users/sharm/Downloads/test/json_data_file.json",'w') as write_file:
    json.dump(json_string,write_file,indent=2)
    
#reading json
with open("C:/Users/sharm/Downloads/test/json_data_file.json",'r') as read_file:
    jdata=json.load(read_file)
    print(type(jdata))
    print(jdata)
    
#JSON in python 
my_data2=json.loads(jdata)
print(type(my_data2))
print(my_data2)

a=urllib2.open('http://www.google.com')