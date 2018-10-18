# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 07:44:04 2018

@author: behzad
"""

def epsilonEffective(epsilon1=0.9, epsilon2=0.9):
    """ This function simply calculates the epsilon effective
    if you don't give the value for epsiln one or two it will consider it
    to be 0.9 by default"""
    result=1/(1/epsilon1+1/epsilon2-1)
    return result


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
    

ThermalResDict = {"FaceBrick":{"R":0.075, "length":0.1}
, "woodStud_90mm":{"R":0.36, "length":0.09}
, "woodFiberBoard":{"R":0.23, "length":0.013}
, "woodLappedSiding":{"R":0.14, "length":0.013}
, "gypsum":{"R":0.079, "length":0.013}
, "insideSurface":{"R":0.12}
, "outsideSurfaceWinter":{"R":0.03}
, "outsideSurfaceSummer":{"R":0.044}
}
