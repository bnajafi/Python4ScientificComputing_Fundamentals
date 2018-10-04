# -*- coding: utf-8 -*-
"""
Created on Thu Oct 04 13:42:26 2018

@author: behzad
"""

R1 = ["R_foam", "cond", 0.06, 0.87, 15]

R1[0][-2]
R1[2]=0.07

Resistance_R1 = R1[2]/(R1[3]*R1[-1])

R1.append(Resistance_R1)


#tuple 
 # tuple is basically lists that can not be changed
 # we don't use it as we always will use lists for these applications

t1 = (0.06,3, "cond")

t1[1] = 4


# Welcome to the world of dictionaries !

dict1 = {"name":"Marco","age":25, "FavoriteMusic":"Rock"}
dict1["name"]


