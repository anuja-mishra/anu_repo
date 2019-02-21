# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:24:40 2018

@author: sharm
"""

#Challenge 1

n=input("Enter a number ")
import math
x=math.factorial(int(n))
print("factorial of number is:",x)

#challenge 2
r=input("enter radius of the circle :")
from math import pi
area= pi* int(r)*int(r)
circum=2*pi*int(r)
print("area is : {} \n and circumference is :{} ".format(area,circum))

#challenge3
help(str.join)
name= input("enter  your first and last name")
res= name.replace(' ',"*")
print(res)

#challenge 4
dir(str)
help(str)
#res= name.lower()

name= input("Enter a  string")
print(name.swapcase())

#challenege 5
str4= 'RESTART'
#print(str4.replace('R','$'))
str7=str4[2:].replace('R','$')
print(str7)

strr=(str4.lstrip('R')).replace('R','$')
print('R'+strr)
#challenege6
str5="anuja sharma"
print(str5)
name= str5.split()
type(name)
resu=' '.join(name[::-1])

print(resu)


#challenge 9

print("\"Anuja\"\n\"sharma\"  ")

#challenge 10
print("26" u'\u00b0')

#challenge 11
print("UNIX" u'\u00AE' " and Sun Microsystems" u'\u2122' " are" u'\u00A9' ", 2018 Oracle")

#challenge 12
print(u'\u0905\u0928\u0941\u091C\u093E  \u0936\u0930\u094D\u092E\u093E')

print(u'\u0935\u093F\u091C\u095F')

#challenege 13
i=1
for i in range(1,9):
    #for c in range(1,5):
            if(i%2==0):
                a= u'\u006f \u002A '
                print(a*4)
            else:
                b=u'\u002A \u006f '
                print(b*4)
                
#challenge 14
def BMI():
    str1="""World Health Organization(WHO) BMI values(8 Levels)
        . Severe Thinness: less than 16
        . Moderate Thinness: between 16 and 16.9
        . Mild Thinness: between 17 and 18.4
        . Normal: between 18.5 and 24.9
        . Overweight: between 25 and 29.9
        . Obese class I : between 30 and 34.9
        . Obese class II: between 35 and 39.9
        . Obese class III: 40  or greater"""
    
    print(str1)
    
    a=input("enter")
    """ 
    weight_hin=input(u'\u0915\u0943\u092A\u094D\u092F\u093E \u0905\u092A\u0928\u093E \u0935\u091C\u0928 \u0907\u0928\u092A\u0941\u091F \u0915\u0930\u0947\u0902')
    height_hin= input(u'\u0915\u0943\u092A\u094D\u092F\u093E \u0905\u092A\u0928\u0940 \u0932\u092E\u094D\u092C\u093E\u0908 \u0907\u0928\u092A\u0941\u091F \u0915\u0930\u0947\u0902')
    weight=float(weight_hin)
    height=float(height_hin)
    res=weight/(height*height)
    print(res)"""
   
    
BMI()


#age calculator

st_age= input("Enter your current age")
age=int(st_age)
fu_yr=input("how many year later you want to know your future age ")
future=int(fu_yr)
pa_yr=input("how many year before you want to know your age")
past=int(pa_yr)
future_age= age+future
past_age= age-past

print("you will be {} years old after {} years \n you were {} year old {} years ago".format(future_age,future,past_age,past) )

#height calculator
def height(hi):
    #height=input("enter your height")
    total= hi.split('.')
    feet=int(total[0])
    inch=int(total[1])
#print(feet)        
    m_feet= feet*0.3048
    m_inch=inch*0.0254
    m_height=m_feet + m_inch
    print("you height converted in meteres is {}".format(m_height))
    return(m_height)
#height()

#bmi calculator
def bmi(weight_hin,h_m):
    
   # weight_hin=input(u'\u0915\u0943\u092A\u094D\u092F\u093E \u0905\u092A\u0928\u093E \u0935\u091C\u0928 \u0907\u0928\u092A\u0941\u091F \u0915\u0930\u0947\u0902')
    #height_hin= input(u'\u0915\u0943\u092A\u094D\u092F\u093E \u0905\u092A\u0928\u0940 \u0932\u092E\u094D\u092C\u093E\u0908 \u0907\u0928\u092A\u0941\u091F \u0915\u0930\u0947\u0902')

    weight=float(weight_hin)
    #h_m=height(height_hin)
#height=float(height_hin)
    res=weight/(h_m)
    bmi=res/h_m
    print("your bmi is {}".format(bmi))
    return bmi
    
#bmi()
  
# height convertor, bmi calculator, ponderal index
def main():
    weight_hin=input(u'\u0915\u0943\u092A\u094D\u092F\u093E \u0905\u092A\u0928\u093E \u0935\u091C\u0928 \u0907\u0928\u092A\u0941\u091F \u0915\u0930\u0947\u0902')
    height_hin= input(u'\u0915\u0943\u092A\u094D\u092F\u093E \u0905\u092A\u0928\u0940 \u0932\u092E\u094D\u092C\u093E\u0908 \u0907\u0928\u092A\u0941\u091F \u0915\u0930\u0947\u0902')

    print("your height in meters")
    h_m=height(height_hin)
    print("you bmi")
    b=bmi(weight_hin,h_m)
    print("Ponderal Index calculator")
    pic= b/h_m
    print("your ponderal Index is {}".format(pic))
main()

# heart rate calculator

age=input("enter your age")
mhr=220-int(age)
l_thr= .70*mhr
h_thr= .85*mhr
print("your maximum heart rate is {} and lower Target heart rate is {} and higher Target heart rate is{}".format(mhr,l_thr,h_thr))

#temperature calculator
temp=input("Enter today's temperature in centigrade")

fah= (int(temp)*(9/5))+32
kel= int(temp)+273
print("temperature in fahrenheit is {}\n temp in kelvin is {} ".format(fah,kel))


#Gas milage calculator
dis= input("enter distance covered in KM before petrol tank of your car was empty")
petrol=input("enter petrol you filled initially")
avg= float(dis)/int(petrol)
print(avg)

#Ride cost calculator

dis=input("total distance covered (to  and fro) in km")
price=input("petrol price per litre")
avg=input("give average of your car")
total_petrol=float(dis)/float(avg)
total_price= total_petrol * float(price)
print(total_price)

#Gravity Calculator

Distance= (-9.81* 10 * 10)/2
print(Distance)

# Weighted Score Calculator

assignment

str1="anuja sharma"

print(str1.strip(" "))
str1.casefold()
