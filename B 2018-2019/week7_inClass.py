# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 13:41:45 2018

@author: behzad
"""

import numpy as np
import pandas as pd

A1=np.array([2,5.2,1.8,5])

S1 = pd.Series([2,5.2,1.8,5],["a","b","c","d"])
S2 = pd.Series([2,5.2,1.8,5],index= ["a","b","c","d"])

S2["c"]

Q_heating = pd.Series([1150,1240,120],index=["wall","ceiling","door"])

# Were you will probabely make mistakes !
# remember that Series (starts with capital S)
# remember the first item ia list you should0nt write it like this: pd.Series(1,3,3,2)
Q_heating["door"]

# of course we can repeat the same procedure we did with arrays

Opaque_item_list = ["wall", "ceiling","door"]

Opaque_U_list = [0.438,0.25,1.78]
opaque_U_Series = pd.Series(Opaque_U_list,index=Opaque_item_list)
opaque_area_list = [105.8,200,2.2]
opaque_area_Series=  pd.Series(opaque_area_list,index=Opaque_item_list)

T_inside_heating= 20
T_outside_heating = -4.8
DeltaT_heating= T_inside_heating-T_outside_heating

opaque_HF_Series = DeltaT_heating*opaque_U_Series
opaque_Q_Series = opaque_HF_Series*opaque_area_Series

# one of very useful pandas capabilities is the apply function !!
def toKwGenerator(inputVal):
    outputVal = inputVal/1000
    return outputVal

Q_heating_kw = opaque_Q_Series.apply(toKwGenerator)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%
#It is a better idea to use a dataframe
Opaque_U_list = [0.438,0.25,1.78]
opaque_area_list = [105.8,200,2.2]
Opaque_item_list = ["wall", "ceiling","door"]
T_inside_heating= 20
T_outside_heating = -4.8
DeltaT_heating= T_inside_heating-T_outside_heating


DF_opaque = pd.DataFrame([Opaque_U_list,opaque_area_list],index=["U","Area"],columns=Opaque_item_list)
DF_opaque.iloc[0,:] # first way
DF_opaque.loc["U",:] # second way
DF_opaque.loc["HF",:] = DF_opaque.loc["U",:]*DeltaT_heating
DF_opaque.loc["Q",:] = DF_opaque.loc["HF",:]*DF_opaque.loc["Area",:]
DF_opaque.loc["Q_kW",:] = DF_opaque.loc["Q",:].apply(toKwGenerator)

import os
os.chdir(r"C:\Users\behzad\Dropbox\2 Teaching Activities\0 EETBS 2018\forked_repos\Python4ScientificComputing_Fundamentals\A 2018-2019")

DF_opaque.to_excel("Q_opaque_results.xlsx")
DF_opaque.to_html("opaque_q_res.html")

DF_input = pd.read_excel("inputData.xlsx",index_col=0,header=0) # these two arguemnts are the dafault , you can change them if you want



def RValue_material(input_material):
    ThermalResDict={"Outside Air":{"R":0.03},
            "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
            "Wood Fiberboard":{"R":0.23,"l":0.013},
            "Glass Fiber Insulation":{"R":0.7,"l":0.025},
            "Wood Stud":{"R":0.63,"l":0.9},
            "Gypsum":{"R":0.079,"l":0.013},
            "Inside Air":{"R":0.12}
            }
    RValue_thisMaterial = ThermalResDict[input_material]["R"]
    return RValue_thisMaterial

def standardLength_material(input_material):
    ThermalResDict={"Outside Air":{"R":0.03},
            "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
            "Wood Fiberboard":{"R":0.23,"l":0.013},
            "Glass Fiber Insulation":{"R":0.7,"l":0.025},
            "Wood Stud":{"R":0.63,"l":0.9},
            "Gypsum":{"R":0.079,"l":0.013},
            "Inside Air":{"R":0.12}
            }
    standardLength_thisMaterial = ThermalResDict[input_material]["l"]
    return standardLength_thisMaterial

RValue_raw = DF_input.loc[:,"Material"].apply(RValue_material)
standardLength_material = DF_input.loc[:,"Material"][DF_input.loc[:,"Type"]=="cond"].apply(standardLength_material)
RValue_corrected = RValue_raw
RValue_corrected[DF_input.loc[:,"Type"]=="cond"]=RValue_corrected[DF_input.loc[:,"Type"]=="cond"]*DF_input.loc[:,"Length"][DF_input.loc[:,"Type"]=="cond"]/standardLength_material
DF_input.loc[:,"Rvalue"] = RValue_corrected
DF_input.to_excel("inputData.xlsx")