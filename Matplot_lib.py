# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:04:19 
"""
#Draw a line graph
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3,3,0.001)
plt.plot(x,norm.pdf(x))

plt.show()

#Multiple plots on One Graph
plt.plot(x, norm.pdf(x)) 
plt.plot(x,norm.pdf(x,1.0,0.5))
plt.show()   

#save it to a file
plt.plot(x, norm.pdf(x)) 
plt.plot(x,norm.pdf(x,1.0,0.5))
plt.savefig('Myplot.png', format='png')

#Adjust the Axes
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,1.0,0.5))
plt.show()

#add a grid
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axes.grid()
plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,1.0,0.5))
plt.show()

#change Line types and colors
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
plt.plot(x,norm.pdf(x),'b-')
plt.plot(x,norm.pdf(x,1.0,0.5),'r-')
plt.show()

#labelling Axes and Adding a Legend
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axes.grid()
plt.xlabel('Greebles')
plt.ylabel('Probability')
plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,1.0,0.5))
plt.legend(['Sneetches','Gacks'],loc=4)
plt.show()

#Pie chart
#plt.rcdefaults()
values=[22,55,4,32,14]
colors=['r','g','b','c','m']
explode=[0,0,0.2,0,0]
labels=['India','US','Russia','China','Europe']
plt.pie(values,colors=colors,labels=labels,explode=explode,autopct='%.2f')
plt.title("Student locations")
plt.show()

#Bar Chart
values=[12,55,4,32,14]
colors=['r','g','b','c','m']
plt.bar(range(0,5),values,color=colors)
plt.show()

#Scatter plot

from pylab import randn
X=randn(500)
Y=randn(500)
plt.scatter(X,Y)
plt.show()

#Histogram
import numpy as np
income=np.random.normal(27000,15000,10000)
plt.hist(income,50)
plt.show()

#Box & Whisker Plot
uniformskewed=np.random.rand(100)*100-40
high_outliers=np.random.rand(10)*50+100
low_outliers=np.random.rand(10)*-50-100
data=np.concatenate((uniformskewed,high_outliers,low_outliers))
plt.boxplot(data)
plt.show()

