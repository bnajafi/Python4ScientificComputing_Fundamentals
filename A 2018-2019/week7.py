# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 06:12:03 2018

@author: behzad
"""

import pandas as pd


Input_DF = pd.read_excel("inputData.xlsx",index_col=0,header=0)


def RValue_material(material):
    ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}
                }
    
    RValue= ThermalResDict[material]["R"]
    return RValue

def  StandardLength_material(material):
    ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}
                }
    
    RValue= ThermalResDict[material]["l"]
    return RValue

Rvalue_raw = Input_DF["Material"].apply(RValue_material)
standardLength_material =  Input_DF["Material"][Input_DF["Type"]=="cond"].apply(StandardLength_material)
Rvalue_final=Rvalue_raw
Rvalue_final[Input_DF["Type"]=="cond"] = Rvalue_final[Input_DF["Type"]=="cond"]*Input_DF["Length"][Input_DF["Type"]=="cond"]/standardLength_material
Input_DF["Rvalue"]=Rvalue_final

Input_DF.to_excel("results.xlsx")