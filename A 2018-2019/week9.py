# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:06:39 2018

@author: behzad
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

X=np.arange(-10,10.1,0.1)
Y=X**2-5

def myFunc(x):
    y=x**2-5
    return y
X_series = pd.Series(X)
Y_series = X_series.apply(myFunc)

plt.figure()
plt.plot(X_series,Y_series)

X3 = np.linspace(0,10,100)
plt.figure()
plt.plot(X3,np.sin(X3),'-')
plt.plot(X3,np.cos(X3),'--')

fig = plt.figure()
plt.plot(X3,np.sin(X3),'-')
plt.plot(X3,np.cos(X3),'--')

WhereToSaveMyFiles = r"C:\Users\behzad\Dropbox\2 Teaching Activities\0 EETBS 2018\forked_repos\Python4ScientificComputing_Fundamentals\A 2018-2019\External Files"
os.chdir(WhereToSaveMyFiles)

fig.savefig("my_figure.png")

# MATLAB Style subplots!
plt.figure()

plt.subplot(2,1,1) # (number of row, number of columns, Number of this item !!)
plt.plot(X3,np.sin(X3),'-')

plt.subplot(2,1,2)
plt.plot(X3,np.cos(X3),'--')

# More elaborate way! (object oriented)

fig,ax  = plt.subplots(2) # Fig is the whole frame !!!, ax is a list each of which is associated with one of the axes !
ax[0].plot(X3,np.sin(X3),'-')
ax[1].plot(X3,np.cos(X3),'--')

# Let's Style stuff !!!
# Let's start with colours

plt.figure()
plt.plot(X3,np.sin(X3 - 0),color="blue") #using name !
plt.plot(X3,np.sin(X3 - 1),color="g") # this is just a short cut (rgbcmyk)
plt.plot(X3,np.sin(X3 - 2),color="0.75") #• gray scale between 0 and 1
plt.plot(X3,np.sin(X3 - 3),color="#FFDD44") # Hex code  RRGGBB
plt.plot(X3,np.sin(X3 - 4),color=(1.0,0.2,0.3) )# RGB tuple:; between 0 ans 1
plt.plot(X3,np.sin(X3 - 5),color="chartreuse") # HTML color code

# Line style
plt.figure()
plt.plot(X3,X3+ 0,linestyle="solid")
plt.plot(X3,X3+ 1,linestyle="dashed")
plt.plot(X3,X3+ 2,linestyle="dashdot")
plt.plot(X3,X3+ 3,linestyle="dotted")

plt.figure()
plt.plot(X3,X3+ 0,linestyle="-")
plt.plot(X3,X3+ 1,linestyle="--")
plt.plot(X3,X3+ 2,linestyle="-.")
plt.plot(X3,X3+ 3,linestyle=":")
 
# if you want to make it faster you can combine color and style

plt.figure()
plt.plot(X3,X3+ 0,"-g")
plt.plot(X3,X3+ 1,"--c")
plt.plot(X3,X3+ 2,"-.k")
plt.plot(X3,X3+ 3,":r")

# How to choose the limits
plt.xlim(2,5)
#plt.ylim(2,6)

plt.xlabel("This is the x axis name")
plt.ylabel("This is the y axis name")
plt.title("this is the title of my figure")

# How to add labels to multiple graphs
plt.figure()
plt.plot(X3,np.sin(X3),"-g", label="sin(x)")
plt.plot(X3,np.cos(X3),":b",label="cos(x)")
plt.legend()

 # How to create scatter plots
plt.figure()
plt.plot(X3,np.sin(X3),"d", color="black")

# the option you have for the markers are:
# o, . , , x, + v > < s d

plt.plot(X3,np.sin(X3),"-ok")

plt.figure()

plt.plot(X3,np.sin(X3), color="gray",
         markersize=15,linewidth=4,
         markerfacecolor="white",
         markeredgecolor="gray",
         markeredgewidth=2
         )

# Scatter using scatter !!!!
plt.figure()
plt.scatter(X3,np.sin(X3),marker="o")

plt.figure()
rng = np.random.RandomState(0)
x=rng.randn(100)
y=rng.randn(100)
colors =rng.randn(100)
sizes = 1000*rng.randn(100)
plt.scatter(x,y,c=colors,s=sizes, alpha=0.3, cmap="viridis")
plt.colorbar()

# How to close the figures!
plt.close("all")

items1= [1,3,5]
items2 = [2,4,6]
labels= ["wall", "floor", "door"]
heatingLoad=[2581,3500,300]
coolingLoad=[2300,3400,250]
fig1 = plt.figure()
plt.bar(items1, heatingLoad,label="Heating Load",color="red")
plt.bar(items2, coolingLoad,label="cooling Load")
plt.legend()
plt.xticks(items1,labels)


#: How to make pie Charts!





