name= "I am Jack"
claim= " and I am awesome "
sentences=20*(name+claim)
print sentences
"""
age= 18
myNewSentence= "I am"+ str(age)
myStringNumber="7"
myNumber= float(myStringNumber)
print "my number is "+str(myNumber)
"""

#R= 0.05#the unit is degC/W

A=12 #m2
L=0.2 #m
#k=raw_input("What is the conductivity of this layer? ")
material=raw_input("What is the material of this layer? ")
if material=="glass":
  print "you just said the material is glass but I have a doubt"
  glassType=int(raw_input("which type of glass did you mean: Enter 1 for window and 2 for insulation"))
  if glassType==1:
        k=0.8
  elif glassType==2:
    k=0.05
  else:
   print "I dont know this type"
  k=float(raw_input("What is the conductivity of this layer? "))
          
elif material=="brick":
    k=2
else:
    print "I don't know this material"
    k=float(raw_input("What is the conductivity of this layer? "))
print "the conductivity of the material is "+str(k)+" W/mK" 
R=L/((k)*A)
print "The resistance of this layer is "+str(R)+ " degC/W"
