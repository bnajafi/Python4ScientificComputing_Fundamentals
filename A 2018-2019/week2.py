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

R1 = {"name":"R_foam", "type":"cond", "length":0.06,
      "conductivity":0.78,"area": 15
      }

R2 = {"name":"R_brick", "type":"cond", "length":0.1,
      "conductivity":0.2,"area": 15
      }

Ressitance_R1 = R1["length"]/(R1["conductivity"]*R1["area"])
R1["resistance"]= Ressitance_R1

ResistanceList = [R1,R2,Ri] # A list of dictionaries

Ri = {"name":"R_i", "type":"conv", "h":9.2,"area": 15 }
fancyResults ={"Rtot":0, "R_foam":.0003}
Rtot=0
for anyResistance in ResistanceList:
    if anyResistance["type"] == "cond":
        RValue = anyResistance["length"]/(anyResistance["conductivity"]*anyResistance["area"])
        anyResistance["RValue"]=RValue
        Rtot=Rtot+RValue
        fancyResults[anyResistance["name"]]=anyResistance["RValue"]
      
    elif anyResistance["type"] == "conv":
        RValue = 1/(anyResistance["h"]*anyResistance["area"])
        anyResistance["RValue"]=RValue
        Rtot=Rtot+RValue
        fancyResults[anyResistance["name"]]=anyResistance["RValue"]

    else:
        print("Pay attentiona that, this resistance does not have a valid type")
        print(anyResistance["name"])
fancyResults["Rtot"] = Rtot    


# LEt's see how we can use every thing we have learned today
#to solve the Example 1 in simplified Wall Calculations lesson

ThermalResDict = {"FaceBrick":{"R":0.075, "length":0.1}
, "woodStud_90mm":{"R":0.36, "length":0.09}
, "woodFiberBoard":{"R":0.23, "length":0.013}
, "woodLappedSiding":{"R":0.14, "length":0.013}
, "gypsum":{"R":0.079, "length":0.013}

, "insideSurface":{"R":0.12}
, "outsideSurfaceWinter":{"R":0.03}
, "outsideSurfaceSummer":{"R":0.044}
}
    
R_6 = {"name":"Gypsum Wallboard","type":"cond","material":"gypsum", "length":0.013}
R_2 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}



ResistanceList_withWood = []



