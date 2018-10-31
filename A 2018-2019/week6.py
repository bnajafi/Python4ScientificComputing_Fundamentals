# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:56:04 2018

@author: behzad
"""

import numpy as np
import pandas as pd 


# what we call a 1 D array in numpy is called a Series in Pandas
S1 = pd.Series([1,2,3,4])
S2= pd.Series([4,5,6,0.1])
S3 = S1+S2
S4 = S1-S2
S5 = S1 > S2

S1[2]
S2[S2>5]

S6 = pd.Series([1,3,6,9],["a","b","c","d"])
S7 = pd.Series([4,5,7,9],["d","b","c","a"])
S8= S6+S7


Q_heating = pd.Series([1150,1240,124],index=["Wall","Ceiling","door"])
# pay attention that wriritng index= is optional - it is better to put it so that you would remember tha the second list is the index

Q_heating["door"]

# One useFul function 
Q_heating.argmax()
# you can also convert the numpy arrays into pandas Series


Opaque_item_list = ["wall", "ceiling","door"]
opaque_item_array = np.array(Opaque_item_list)

Opaque_U_list = [0.438,0.25,1.78]
opaque_U_array = np.array(Opaque_U_list)

opaque_area_array = np.array([105.8,200,2.2])

T_inside_heating= 20
T_outside_heating = -4.8
DeltaT_heating= T_inside_heating-T_outside_heating
opaque_HF_array = DeltaT_heating*opaque_U_array
opaque_Q_array = opaque_HF_array*opaque_area_array

Q_heating=pd.Series(opaque_Q_array, index=opaque_item_array)
Q_heating["wall"]

# using Apply and functions
def toKw(inputValue):
    outputValue = inputValue/1000
    return outputValue

Q_heating_kw =  Q_heating.apply(toKw) 
# The alternative way of doing this was to use a for and apply this on all elements but it takes longer time to write and longer time to run
Q_heating_wall = toKw( Q_heating["wall"]) 


# Let's See how to define 2D matrix: In pandas we call this Data Frame 

resistance_names = ["R1","R2","R3","R4","R5"]
resistances_types = ["conv","cond","cond","cond","conv"]
resistances_h = [10,None,None,None,25]
resistances_k=  [None,0.8,1.5,0.05,None]
resistances_L= [None,0.5,0.3,0.6,None]
resistances_RValues=[0,0,0,0,0]



