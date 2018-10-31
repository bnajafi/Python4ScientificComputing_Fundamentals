# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 07:31:52 2018

@author: behzad
"""
import numpy as np

#' The main use of numpy is defining arrays ---These are vectors !!

A1 = np.array([1,4,5,11]) # An array of integers
A2 = np.array([1.2,5.0,9.3,5])
A1.dtype
A2.dtype
# All of the elements of an array should have the same type !
# If they don't numpy will conver them 

A3 = np.array(["marco", "mirko", "sara"])
A4 = np.array([True,False, False, True])

A3.dtype
A5 = np.array([1, "manuel", 4.5])

# This is definitely a disadvantage because it will change it by itself and it
# it will create a mess !!!
L6 = [1.4,5.3,7.6]
L7 = [2.2,3.0, 9.5]
A6 = np.array(L6)
A7 = np.array(L7)

L8=L6+L7 # We don't want this !!!!
A8 = A6+ A7 # This does vectorized operation

A9 = A6 - A7

A10=A6*A7

L11 = 2*L6 #☻ We do not want this !!!
A11 = 2* A6

# LEt's use it to solve our probelms !! RLF method !

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


# Element extraction 
opaque_Q_array[0]
opaque_Q_array[0:2]
opaque_Q_array[-1]

opaque_Q_array[-1]=0 # You can assign values 

#Logical arrays !!
TheOneMoreThan1000 = opaque_Q_array > 1000

A12 = np.array([3,5,7,11])
A13 = A12 > 5
A14 = A12<5

opaque_item_array == "wall"

A12[A14]

index_wall = opaque_item_array == "wall"
indeX_ceiling  = opaque_item_array == "ceiling"
index_wallOrCeiling = index_wall | indeX_ceiling

opaque_Q_array[opaque_item_array == "wall"]
Opaque_wallOrCeiling_value = opaque_Q_array[index_wallOrCeiling].sum()
SumOfAll_opaqueHearting =opaque_Q_array.sum()
AverageOfAll_opaqueHeating=opaque_Q_array.mean()


# Let's use this approach to solve the problem of resistances
Ri = ["R_internal","conv", 8.9, 15]
R1 = ["R_foam","cond", 0.06, 0.05, 15]
R2 = ["R_wood","cond", 0.1, 0.4, 15]
R3 = ["R_plaster","cond", 0.01, 1, 15]
Ro = ["R_external","conv", 20, 15]

resistance_names = np.array(["R_internal","R_foam","R_wood","R_plaster","R_external"])
resistance_types = np.array(["conv","cond","cond","cond","conv"])
resistance_k = np.array([ None,0.05,0.4,1,None])
resistance_L = np.array([ None,0.06,0.1,0.01,None])
resistance_A = np.array([ 15,15,15,15,15])
resistance_h = np.array([ 8.9,None,None,None,20])

resistance_RValues= np.array(np.zeros(5))

resistance_RValues[resistance_types=="cond"]=resistance_L[resistance_types=="cond"]/(resistance_k[resistance_types=="cond"]*resistance_A[resistance_types=="cond"])
resistance_RValues[resistance_types=="conv"]=1.0/(resistance_h[resistance_types=="conv"]*resistance_A[resistance_types=="conv"])
Rtot=resistance_RValues.sum()


# Let's define 2D arrays : Matrices
L1 = [1.2,3.3,4.5]
L2 = [3.9,4.3,2.2]
L3 = [2.2,3.2,3.9]

AA1 = np.array([L1,[3.9,4.3,2.2],L3]) # pay attention that we are defining lists inside other lists

AA1[:,1]

AA1[2,:]


AA1.sum()

AA1.sum(axis=0)
AA1.sum(axis=1)





