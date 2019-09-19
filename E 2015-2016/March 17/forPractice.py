#def factorial(n):
    #result =1
    #while n>0:
   #  result=result*n
  #  n=n-1
 #   return y ***
 
 
#R_string = raw_input("What is the Resistances")
#R= float(R_string)
#print("The Resistance is determined to be" +str(R)+ "degC/W")


#B_string= raw_input("What is the type of material (Metals/m):")
#B=(B_string)
#material=raw_input("The material")
#if material=="glass":
#     k=0.9   
#print("The conductivity of the mat is "+str(k)+" ")     


#input_d=raw_input("Please enter the layers conductivity")
#print("You just told me that the conductivity is " +input_d+ " W/(m.degC)")


#Simple script

L= raw_input("What is the Length of the wood( in m):")
A=raw_input("What is the Area of the wood(in m2):")
k=raw_input("The conductivity of the material(in W/mdeg.C):")
R= (float(k)*float(A))/float(L)
print("The Resistance of the material is " +str(R)+ " W/m2.deg.C")
