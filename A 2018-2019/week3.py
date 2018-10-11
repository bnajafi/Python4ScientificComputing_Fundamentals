# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 07:32:00 2018

@author: behzad
"""

def PowerOFN(x,n=2):
    y=x**n
    return y

PowerOFN(x=2)

def epsilonEffective(epsilon1=0.9, epsilon2=0.9):
    """ This function simply calculates the epsilon effective
    if you don't give the value for epsiln one or two it will consider it
    to be 0.9 by default"""
    result=1/(1/epsilon1+1/epsilon2-1)
    return result

epsilonEffective(0.05)

#myEpsilons=range(1,101,2)

myEpsilons = [0.05,0.3,0.7,0.12,0.2,0.25,0.50,0.9,0.84]
for mirko in myEpsilons:
    print(epsilonEffective(epsilon1=mirko))
    
help(epsilonEffective)  
# Second way 
epsilonEffective.__doc__


def epsilonEffectiveVectorialOtherOneNormalWall(ListOfEpsilons):
    """ This function simply calculates the epsilon effective
    for a list of emissivities while the other one is a normal wall
    it returns a list of effective epsilons"""
    epsilon2= 0.9
    ListOFEffectiveEpsilons= []
    for anyEpsilon in ListOfEpsilons:
        result=1/(1/anyEpsilon+1/epsilon2-1)
        ListOFEffectiveEpsilons.append(result)
    return ListOFEffectiveEpsilons
    
epsilonEffectiveVectorialOtherOneNormalWall(myEpsilons)


# How to use this methodology to calculate the thermal resistance of a series of layers

ThermalResDict = {"FaceBrick":{"R":0.075, "length":0.1}
, "woodStud_90mm":{"R":0.36, "length":0.09}
, "woodFiberBoard":{"R":0.23, "length":0.013}
, "woodLappedSiding":{"R":0.14, "length":0.013}
, "gypsum":{"R":0.079, "length":0.013}
, "insideSurface":{"R":0.12}
, "outsideSurfaceWinter":{"R":0.03}
, "outsideSurfaceSummer":{"R":0.044}
}

AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23},
               0.040:{0.03:0.063,0.05:0.59,0.5:0.25}}
AirGapResDict[0.02][0.03]

AirGapResDict[0.04][0.5]


R_6 = {"name":"Gypsum Wallboard","type":"cond","material":"gypsum", "length":0.013}
R_2 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}
R_i =  {"name":"inside surface","type":"conv","material":"insideSurface"}
R_gap ={"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}
ResistanceList_withWood = [R_i,R_2,R_6,R_gap]

def ResistanceOfLayersInSeries(ListOfResistances):
    ThermalResDict = {"FaceBrick":{"R":0.075, "length":0.1}
    , "woodStud_90mm":{"R":0.36, "length":0.09}
    , "woodFiberBoard":{"R":0.23, "length":0.013}
    , "woodLappedSiding":{"R":0.14, "length":0.013}
    , "gypsum":{"R":0.079, "length":0.013}
    , "insideSurface":{"R":0.12}
    , "outsideSurfaceWinter":{"R":0.03}
    , "outsideSurfaceSummer":{"R":0.044}
    }
    
    AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23},
                   0.040:{0.03:0.063,0.05:0.59,0.5:0.25}}
    ResultsDictionary={}
    Rtot=0
    for anyResistance in ListOfResistances:
        if anyResistance["type"]=="cond":
            material_anyResistance = anyResistance["material"]
            length_anyResistance = anyResistance["length"]
            lengthOfThisMaterialInTheLibrary = ThermalResDict[material_anyResistance]["length"]
            RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
            anyResistance["RValue"]=RValue_anyResistance
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
            Rtot=Rtot+RValue_anyResistance
        elif anyResistance["type"]=="conv":
            material_anyResistance = anyResistance["material"]
            RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]
            anyResistance["RValue"]=RValue_anyResistance   
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
            Rtot=Rtot+RValue_anyResistance
        elif anyResistance["type"]=="gap":
            effectiveEpsilon=epsilonEffective(anyResistance["epsilon1"],anyResistance["epsilon2"])
            RValue_anyResistance = AirGapResDict[anyResistance["length"]][effectiveEpsilon]
            anyResistance["RValue"]=RValue_anyResistance 
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
            Rtot=Rtot+RValue_anyResistance
    ResultsDictionary["Rtot"]=Rtot
    return ResultsDictionary



               
    
