# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:14:33 2018

@author: sharm
"""
from PIL import Image, ImageOps
img= Image.open("C:/Users/sharm/Downloads/test/Image1.jpg")

img_name=input("enter image name")
img.save(img_name +".jpg")    

new_img=Image.open(img_name +".jpg")

#rotate 90degree
new_img.rotate(90).save(img_name +".jpg")



#create thumbnail
new_img.thumbnail((75,75))
new_img.save(img_name +".jpg")


#crop image
print(new_img.size)


#new_img.crop((27,27,160,204)).save(img_name +".jpg")


ImageOps.fit(new_img,(160,204), centering=(0.5,0.5)).save(img_name +".jpg")


#greyscale

new_img.convert('L').save(img_name +".jpg")
#alternate way
from PIL.ImageOps import grayscale
grayscale(new_img).save(img_name +".jpg")

new_img.show()

