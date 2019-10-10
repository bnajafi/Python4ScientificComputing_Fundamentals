#!/usr/bin/env python
# coding: utf-8

# # Functions !!
# 

# In[1]:


def PowerOfN(x,n):
    y = x**n
    z = y+3
    return y


# In[5]:


result = PowerOfN(x=3,n=2)


# In[11]:


def PowerOfNV2(x,n=2):
    y = x**n
    z = y+3
    return y




# In[12]:


print(PowerOfNV2(x=5, n=3))



# In[17]:


def epsilonEffective(epsilon1 = 0.9,epsilon2= 0.9):
    """This Function simply calculates the epsilon effective, if you don not
    specifiy the values it considers them to be 0.9 by default"""
    
    result =  1.0/(1/epsilon1+1/epsilon2-1) # here I just implement the epsilon effective formula
    return result

    
    


# In[ ]:





# In[18]:


myResult = epsilonEffective(epsilon1 = 0.05)
print(myResult)


# In[ ]:





# In[ ]:





# In[19]:


help(epsilonEffective)


# In[21]:


myEpsilons = [0.05,0.3,0.7, 0.12,0.5,0.9]
MyEffectiveEpsilons = []
for rafael in myEpsilons:
    MyEffectiveEpsilons.append(epsilonEffective(rafael))
print(MyEffectiveEpsilons)
    


# In[ ]:





# In[22]:


def epsilonEffectiveVectorialOtherBuildingMat(receivedListOFepsilons):
    """This function receives a list of emissivities and find the corresponding 
    effective emissivity in case the other side would be building material -> epsilon = 0.9
    """
    calculatedepsilonEffectiveS = []
    epsilon2 = 0.9 # fixed value 
    for epsilon1 in receivedListOFepsilons:
        epsilonEffective =1.0/(1/epsilon1+1/epsilon2-1) 
        calculatedepsilonEffectiveS.append(epsilonEffective)
        
    return calculatedepsilonEffectiveS


# In[25]:


santiagosNewListOFEps = [0.8,0.7,0.3]
outPutResultsOFEffectiveEps = epsilonEffectiveVectorialOtherBuildingMat(santiagosNewListOFEps)
print(outPutResultsOFEffectiveEps)


# In[ ]:





def ResitanceCalculatorWithLibrary(ListOfResistances):
    ThermalResDict = {"FaceBrick":{"R":0.075, "length":0.1}
    , "woodStud_90mm":{"R":0.36, "length":0.09}
    , "woodFiberBoard":{"R":0.23, "length":0.013}
    , "woodLappedSiding":{"R":0.14, "length":0.013}
    , "gypsum":{"R":0.079, "length":0.013}
    , "insideSurface":{"R":0.12}
    , "outsideSurfaceWinter":{"R":0.03}
    , "outsideSurfaceSummer":{"R":0.044}
    }
    
    
    

    
    


# In[ ]:


R_6 = {"name":"Gypsum Wallboard","type":"cond","material":"gypsum", "length":0.013}
R_2 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}
R_i =  {"name":"inside surface","type":"conv","material":"insideSurface"}

resistancList = [R_6, R_2,R_i]

