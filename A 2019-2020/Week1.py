#!/usr/bin/env python
# coding: utf-8

# ### Reminder Regarding dividing stuff in Python:
# IF you divide two integers: python considers this as an integer division !
# dividing one float by an integer: the result is always a float -> so we should convert one of them to float !

# In[8]:


L = 2
#k = 0.78 # float
k = 1
A = 50

R= float(L) /(k*A)

print(R)






# ### reviewing Strings !



name1 = "Santiago "
type(name1)
name2 = "Luca"
name3= 5 * name2
namesInOrder = name1 + name2
print(name3)
print("The value of R is "+str(R)+" DegC/W") # this just prints the R value


# In[21]:


f = 1
f=float(f)


# In[22]:


f = 21





L_string = raw_input("Please insert the length of this layer: ")
k = 0.78
A = 50

L_val  = float(L_string)
print(L_val)
R= L_val/(k*A)
print(R)




L_string


# In[31]:


L = float(raw_input("Please insert the length of this layer: "))
k = 0.78
A = 50
R= L/(k*A)
print(R)


# ## Control : If statement 
# Let's create a stupid and simple material library



component= "wood 90mm"
if component == "glass 6mm":
    k = 0.95  #W/mK
    L = 0.006 #m
    print("Hi there!")
elif component == "wood 90mm":
    k= 0.4 #W/mK
    L= 0.09 #W/mK
    print("Hi there I am wood!")
else:
    print("I am sorry I dont have this material's properties ")
    
    


# In[42]:


component == "wood 90mm"


# In[46]:


age =int(raw_input("please insert your age: "))
if age < 18:
    print("you are just a kid!")
elif (age>17 and age<30):
    print("Enjoy it!")
else:
    print("The slope is downwards! sorry!")


# ### review of indexes in strings

# In[53]:


name = "Santiago"
print(name[0])
print(name[-2])
print(name[0:2])
print(name[1:])
print(name[3:-1])
print(name[:4])


# ## Lists !!!

# In[61]:


L1 = [17,28,34,48]
print(L1[2])
print(L1[1:3])
print(L1[:2])


# In[63]:


names = ["Luca","Santiago","Sara","Luigi","John"]


# In[67]:


print(names[1:3])
print(names[1][3:5])


# In[68]:


print(names[2][-2:])


# In[69]:


L2 = ["Santiago",4, 8.9, False]


# In[70]:


print(L2[2])


# In[77]:


L2[0] = 1
L2


# In[84]:


L2[-1]=10
##L2[4] = 11  #this does not work, you should use append
L2.append(11) # adds it at the end 


# In[88]:


L2.insert(2,12) # index and then element
L2


# In[89]:


R1 = ["R_Foam","cond",0.06, 0.78,15]


# In[98]:


R1 = ["R_Foam","cond",0.06, 0.78,15]
#L_R1 = R1[2]
#k_R1 = R1[3]
#A_R1 = R1[4]
#R_Value = float(L_R1)/(k_R1*A_R1)
R_Value = float(R1[2])/(R1[3]*R1[4])
R1.append(R_Value)
print(R1)

R1 = ["R_Foam","cond",0.06, 0.78,15]


# In[100]:


R1 = ["R_Foam","cond",0.06, 0.045,15]
R2 = ["R_wood","cond",0.1, 0.6,15]
R3 = ["R_plaster","cond",0.01, 1,15]


# ## For loop

# In[ ]:





# In[91]:


L1 = [1,2,5,7]
for philippe in L1:
    print(philippe)
    

    


# In[93]:


for anyItem in L1:
    print(anyItem) 


# In[102]:


ResistancesList = [R1,R2,R3] 
print(ResistancesList)
print(ResistancesList[0][-1])


# In[114]:


R1 = ["R_Foam","cond",0.06, 0.045,15]
R2 = ["R_wood","cond",0.1, 0.6,15]
R3 = ["R_plaster","cond",0.01, 1,15]
ResistancesList = [R1,R2,R3] 
R_total = 0
for anyResistance in ResistancesList:
    #print(anyResistance)
    R_Value = float(anyResistance[2])/(anyResistance[3]*anyResistance[4])
    R_total = R_total+R_Value
    anyResistance.append(R_Value)
print(ResistancesList)    
print("the total resistance is "+str(R_total)+ "degC/w")
    
 # what if we have convective resistances!
R_internal = ["R_internal","conv",10,15]
R_external = ["R_external","conv",40,15]

R_value  = 1/(R_internal[2]*R_internal[3])
    
ResistancesList = [R_internal,R1,R2,R3,R_external] 


for anyResistance in ResistancesList:
    #print(anyResistance)
    if anyResistance[1]=="cond":
        R_Value = float(anyResistance[2])/(anyResistance[3]*anyResistance[4])
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
    elif anyResistance[1]=="conv":
        R_value  = 1/(anyResistance[2]*anyResistance[3])
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
        
print(ResistancesList)    

print("the total resistance is "+str(R_total)+ "degC/w")
    
   

