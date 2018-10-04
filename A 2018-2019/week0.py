# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:14:11 2018

@author: behzad
"""

L = 0.05  # this is the length in m
A = 0.22 # area in m2
k= 0.78 #N conductivity W/mK

R_cond = L/(k*A) # resistance on C/W


h_i=  10 # w/m^2 K
R_conv_i = 1/(h_i*A)



h_0=  40 # w/m^2 K
R_conv_o = 1/(h_0*A)




name1= "Manuel"
# multiplying stings!!!
3*name1

# summing up strings
sentence = "my name is "+ name1
sentene2 = "three of us are "+ 3*name1

sentence3 = "The result is "+str(1)

print("The internal convective resistance is "+str(R_conv_i))
print("The external convective resistance is "+str(R_conv_o))
print("The glasse's conductive resistance is "+str(R_cond))

