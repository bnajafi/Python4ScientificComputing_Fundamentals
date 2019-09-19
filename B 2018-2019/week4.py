# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 07:31:52 2018

@author: behzad
"""
import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory) # this will tell python to change directory to the folder where I ran this file

print os.getcwd() # here I just check by printing get current working directoy

# How can Importing other modules be usefull
import random as rn

names =["Mirko", "federica","manuel","Gilberto"]
UnluckyOne = rn.choice(names)

RandomNumber = 1+int(10*rn.random())

RandomNumberII = rn.randrange(20,40)

import os
currentDirectory=os.getcwd() #♦ it stands for get current direcotry which means tell me in which folder I am now 

FolderOfMyWallCalculation=r"C:\Users\behzad\Dropbox\2 Teaching Activities\0 EETBS 2018\forked_repos\Python4ScientificComputing_Fundamentals\A 2018-2019"
os.chdir(FolderOfMyWallCalculation) # it stands for changed direcotry, it measn move the crrent directory to this folder from which I want to import the files
import wallFunctions

os.chdir(currentDirectory)  # this means change the current directory to where i was before 

print(wallFunctions.ThermalResDict)

epsilon1=0.8
epsilon2=0.7
myepsilonEffective= wallFunctions.epsilonEffective(epsilon1,epsilon2)


myEpsilons = [0.05,0.3,0.7,0.12,0.2,0.25,0.50,0.9,0.84]
result=wallFunctions.epsilonEffectiveVectorialOtherOneNormalWall(myEpsilons)

import wallFunctions as wallF
result=wallF.epsilonEffectiveVectorialOtherOneNormalWall(myEpsilons)

from wallFunctions import epsilonEffective,ThermalResDict
from wallFunctions import *

myepsilonEffective= epsilonEffective(epsilon1,epsilon2)
print(ThermalResDict)
result=epsilonEffectiveVectorialOtherOneNormalWall(myEpsilons)


