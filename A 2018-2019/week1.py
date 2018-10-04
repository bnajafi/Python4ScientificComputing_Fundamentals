# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:40:21 2018

@author: behzad

"""
# Let's review 

# different object 
type(2)
type(2.0)
type(True)

#type casting 
 x= float(2)
 
 L= 2
 k=3
 r = float(L)/k
 
 # boolean operations
 True and True 
 True and False 
 False or False 
  not True
  
  x=3
  x>4
  
  y = 12
  y < 15
  
  (x>7) and (y>20)
  x!=5
  
  # basics of strings 
  str1= "Marco "
  str2 = "Sara"
  
  str3=str1+str2
  str4= 4*str1

R= 0.65
print("the value of resistance is "+str(R))


#we are done with the boring review, Let's start new stuff

# what we did previously was this
L = 0.03
A=15
k=0.7

R=float(L)/(k*A)
print("the value of resistance is "+str(R))
# How can we ask the user to give us these values

L_string = raw_input("please insert the length of this layer: ")
k_string = raw_input("please insert the conductivity of this layer: ")
A_string = raw_input("please insert the area of this layer: ")

R = float(L_string)/(float(k_string)*float(A_string))
print("the value of resistance is "+str(R))


# How can we check for conditions 
L_string = raw_input("please insert the length of this layer: ")
material = raw_input("please insert the material of this layer: ")
A_string = raw_input("please insert the area of this layer: ")

if material=="glass":
    k=0.95
elif material=="brick":
    k=0.6
elif material=="wood":
    k=0.4
else:
    k=float(raw_input("Sorry I dont know this material ! please insert the conductivity of this layer: "))
    
 
R = float(L_string)/(k*float(A_string))
print("the value of resistance is "+str(R))
   
# LEt make it better
component = raw_input("please insert the construction component of this layer: ")
A_string = raw_input("please insert the area of this layer: ")

if component=="glass 6mm":
    k=0.95 # W/mK
    L=0.006  #m
elif component=="brick 13mm":
    k=0.6 # W/mK
    L=0.013 #m
elif component=="wood 90":
    k=0.4
    L=0.09
else:
    k=float(raw_input("Sorry I dont know this compoennt ! please insert the conductivity of this layer: "))
    L=float(raw_input("Sorry I dont know this component ! please insert the conductivity of this layer: "))
    
R = L/(k*float(A_string))
print("the value of resistance is "+str(R))


age = int(raw_input("please insert your age: ")
if age < 18:
    print("you are just a kid !")
elif age>18 and age<30:
    print("enjoy it ")
else: 
    print("the slope is downwards!! you know that! ")
     



# Let's talk about strings more !
    
    
# variable naming standards ! you can never use space and it can not start with number!
# use _ or camel notations
#string_inserted
#stringInsertedHereForNoRealReason
    
string_insertedName= "Marco"
string_insertedName[0]
string_insertedName[3]

# NEgative values start from the end
string_insertedName[-2]

# How to choose a range

string_insertedName[1:3] # it give me from (included) till (excluded)

string_insertedName[:2] # it give me from (included) till (excluded)

    
string_insertedName[3:]  


string2 = "Polimi"
string2[2:4]

# Now let's see the next compound object that is more useful !
# Let's use lists !!!
L1 = [17,28,34,48]
L1[1]
L1[-1]
L1[:2]

names=["Marco", "Sara", "Luigi"]

names[-1]

Mix = ["marco", 34,True, 45.0]
Mix[1]=28

Mix[2]=0

Mix[4] = 60 # we can not do this !!!

Mix.append(3)


R1 = ["cond", 0.06, 0.78, 15]

names=["Marco", "Sara", "Luigi"]
for anyElement in names:
    print("Hi "+anyElement+ " !")
    
numbers = [1,23,17,5,86]
for mirko in numbers[:3]mkdir:
    print "the number is "+str(mirko)

R1 = ["R_foam","cond", 0.06, 0.78, 15]

L_thisLayer=R1[2]  
k_thisLayer=R1[3]    
A_thisLayer=R1[-1]   

resistance_thisLayer= float(L_thisLayer)/(k_thisLayer*A_thisLayer) 

R1.append(resistance_thisLayer)

Ri = ["R_internal","conv", 8.9, 15]

  
h_thisLayer=Ri[2]    
A_thisLayer=R1[-1]   

resistance_thisLayer= 1/(h_thisLayer*A_thisLayer)
Ri.append(resistance_thisLayer)

R1 = ["R_foam","cond", 0.06, 0.05, 15]
R2 = ["R_wood","cond", 0.1, 0.4, 15]
R3 = ["R_plaster","cond", 0.01, 1, 15]

ListOfResistances = [R1,R2,R3]
R_total = 0
for anyResistance in ListOfResistances:
    L=anyResistance[2]  
    k=anyResistance[3]    
    A=anyResistance[-1] 
    print("name: "+anyResistance[0])
    print("type: "+anyResistance[1])    
    print("L: "+str(L))
    print("k: "+str(k))
    print("A: "+str(A)) 
    R_thisResistance= float(L)/(k*A)
    R_total=R_total+R_thisResistance
    print("R: "+str(R_thisResistance)+ " degC/W") 
    anyResistance.append(R_thisResistance)
    print("*************************") 
print("total R: "+str(R_total)+ " degC/W") 


for anyResistance in ListOfResistances:
    if anyResistance[1]=="cond":
        L=anyResistance[2]  
        k=anyResistance[3]    
        A=anyResistance[-1] 
        print("name: "+anyResistance[0])
        print("type: "+anyResistance[1])    
        print("L: "+str(L))
        print("k: "+str(k))
        print("A: "+str(A)) 
        R_thisResistance= float(L)/(k*A)
        R_total=R_total+R_thisResistance
        print("R: "+str(R_thisResistance)+ " degC/W") 
        anyResistance.append(R_thisResistance)
        print("*************************") 
print("total R: "+str(R_total)+ " degC/W") 

    
    

    
